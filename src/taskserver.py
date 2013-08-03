# -*- coding:utf-8 -*-

# revisions:
'''
TaskServer
管理计划，执行任务

'''

import sys,os,os.path,traceback,threading,time,datetime,json

import utils
import newgis

'''
Action - 单向链表结构，适用于串行执行动作
'''
class TaskAction:
	WILL_EXEC = 0
	EXEC_DONE = 1
	def __init__(self,task,exctime,act):
		self.task = task
		self.type = act['type']  #action type, 'mail,sms,pushuser...'
		self.exctime = exctime
		self.status = 0 	# 0 - 未执行,1 -已执行
		self.params= act['params']
		self.cfg = act


	#		内置标志 $time - 当前时间
	#		$ao - 设备对象名称
	#		$reason - 报警触发内容
	def makeContent(self,content):
		c=''
		try:
			name = self.task.asi.r['name'].strip()
			reason = self.task.asi.getText().strip()
#			print aoname
			name = name.decode('utf8').strip()
#			print aoname
			c = content
			c = c.replace('$name',name)


			c = c.replace('$time',utils.formatDateTime_ymdhm(datetime.datetime.now()))
			c = c.replace('$reason',reason)
			ao = self.getActiveObject(self.task.asi.aoid)
			if ao:
				c = c.replace('$aoname',ao['name'].decode('utf8'))
		except:
			self.task.getLog().debug(traceback.format_exc())
		return c

	def send_mail(self,tolist,content):
		import sendmail
		tolist = tolist.split(',')
		sendmail.send_mail(tolist,u'报警通知',content)
		self.task.getLog().debug('send mail ok')

	def send_sms(self,tolist,content):
		tolist = tolist.split(',')
		for item in tolist:
			item = item.strip()
			if not item: continue
			self.task.server.ctrlsvr.getSmsService().sendSms(item,content)

		self.task.getLog().debug('send sms ok')

	def getActiveObject(self,aoid):
		ao = self.task.server.ctrlsvr.getActiveObject(aoid)
		return ao

	def execute(self):
		try:
			#报警联动
			target = self.params['tolist']
			text = self.params['content']
			text = self.makeContent(text)
			delta=''
			if self.type =='mail':
				self.send_mail(target,text)
			elif self.type =='sms':
				self.send_sms(target,text)
			elif self.type == 'asi_detach': #撤消报警
				self.task.asi_detach()
				target = u'撤消报警设置'
				text = target

			#默认发送到系统客户端 ctrlserver->dgw->flex user
			#写入报警日志表
			db = self.task.server.getDBConn()
			id = utils.getdbseq(db,'giscore_ao_alarmactionlog_id_seq')
			sql = " insert into giscore_ao_alarmactionlog values(%s,%s,%s,%s,%s,%s,%s)"


			ps = (id,self.task.id,datetime.datetime.now(),self.type,target,text,delta)

			cr = db.cursor()
			cr.execute(sql,ps)
			db.commit()
		except:
			traceback.print_exc()
	
#	def head(self):
#		act = self
#		while act.prev:
#			act = act.prev
#		return act
#
#
#	def tail(self):
#		act = self
#		while act.next:
#			act = act.next
#		return act
	
#task是一维的，action是第二维的	


#任务项包含并行执行和串行执行的action
'''
 task1
    -action1.1 & action1.2 & action1.3
    -action2
    -action3
    ...
对于计划周期性的任务可以在系统启动时和每天凌晨更替时产生Actions
'''
class Tasklet:
	def __init__(self,server=None):
		self.actions = []
		self.mtxthis = threading.Lock()
		self.server = server
		self.asi = None
		self.terminated = False
		self.id = 0

	#初始化任务对象 ，分解action到链表
	def init(self,asi):
		self.asi = asi
		actions = self.asi.actions
		starttime = time.time()
		#acton之间是并行执行，action的多次是串行执行
		# 串行action形成一个单项链表来执行
		for act in actions:
			#根据action.times,freq来创建多个action,并加入到队列
			ta = None
			freq = act['freq']
			self.getLog().debug('prepare action:',act['type'])
			for n in range(act['times']): #
				ta = TaskAction(self,starttime + n*freq,act)
				self.actions.append(ta) #添加一个链表
				self.getLog().debug('push action into taskqueue exctime:',ta.exctime)
		return True

	def getLog(self):
		return self.server.getLogger()

	def asi_detach(self):
		try:
			aoid = self.asi.aoid
			asid = self.asi.r['id']
			db = self.server.getDBConn()
			cur = db.cursor()
			sql = "delete from giscore_activeobject_alarmsettings where activeobject_id=%s and ao_useralarmsettings_id=%s"
			cur.execute(sql,(aoid,asid))
			db.commit()
			self.server.ctrlsvr.getAlarmServer().asi_remove(asid,aoid)
			self.getLog().debug('asi detached:',aoid,asid)
		except:
			self.getLog().debug( traceback.format_exc())

	def execute(self):
		dolist=[]
		backlist=[]
		self.mtxthis.acquire()
		for act in self.actions:
			if int(time.time()) >= act.exctime:
				dolist.append(act)
			else:
				backlist.append(act)
		self.actions = backlist
		self.mtxthis.release()

#		开始执行
		for act in dolist:
			act.execute()
			self.getLog().debug('action ',act.type,' be excuted!')

		if self.terminated: #被外部终止 from asi
			return False #无需继续执行动作

		if len(self.actions) == 0:
			return False #没有可执行的动作了

		return True


#taskserver 任务服务器，执行报警联动和系统计划任务执行	
class TaskServer:
	def __init__(self,ctrlsvr):
		self.ctrlsvr = ctrlsvr

		self.taskes = []
		self.mtxtask = threading.Lock()

		self.threads = utils.ThreadGroup(self._thread_exec)
		
	def getLogger(self):
		return self.ctrlsvr.getLog()
	
	def getDBConn(self):
		return self.ctrlsvr.getDBConn()

	def _thread_exec(self,*p):
		while True:
			self._execTask()
			time.sleep(1)

	def _execTask(self):
		task = None
		self.mtxtask.acquire()
		if len(self.taskes):
			task = self.taskes[0]
			del self.taskes[0]
		self.mtxtask.release()

		if not task:
			return

		r = task.execute()
		if r: #重新置入执行队列
			self.mtxtask.acquire()
			self.taskes.append(task)
			self.mtxtask.release()
			return

	def start(self):
		self.threads.start()
		
	#由报警项创建执行任务
	def createTaskWithASI(self,asi):
#		记录报警触发时间到表
		try:
			task = Tasklet(self)
			task.init(asi)

			self.mtxtask.acquire()
			self.taskes.append(task)
			self.mtxtask.release()
			#记录到数据库
			db = self.getDBConn()
			id = utils.getdbseq(db,'giscore_ao_alarmlog_id_seq')
			sql = " insert into giscore_ao_alarmlog values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			filter = asi.r['filter']
			actions = asi.r['actions']
			ps = (id,asi.aoid,asi.r['name'],filter,actions,
				asi.getText(),'',datetime.datetime.now(),'')
			cr = db.cursor()
			cr.execute(sql,ps)
			db.commit()
			task.id = id
			#发送到flex user
#			m = MsgAoAlarm_Trigger_10()
#			m['aoid'] = asi.aoid
#			m['aoname'] = asi.r['aoname']
#			m['asiname'] = asi.r['name']
#			m['time'] = int(time.time())
#			m['filter'] = filter
##			self.ctrlsvr.sendto_dgw(m)
			alarm = newgis.AlarmInfo_t()
			self.ctrlsvr.usersvc.sendAlarmToUser(alarm)
		except:
			traceback.print_exc()
			return False
		return True
	


if __name__=='__main__':
	pass

	
		
	