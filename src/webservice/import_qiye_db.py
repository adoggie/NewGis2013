# -- coding:utf-8 --

#initdb.py
#导入企业信息到表
#----------------------------------------------------------------------------#


import socket,traceback,os,os.path,sys,time,struct,base64,gzip,array,threading,json

from ConfigParser import ConfigParser
from mutex import mutex as Mutex
import string

#----------------------------------------------------------------------------#
aolist=[
		{ 'name':'K.5H773','dasid':'das001','running':0,'iconurl':'null',
			'modules':[
				{'type':1,'sid':'013661940344','svcname':'ts108',
				'settings':{'acc_on_freq':30,		
							'acc_off_freq':15,
							'sample_contined':{'freq':10,'duration':0}
							}
				}, #gps模拟模块1
				#sid - 设备唯一编号 0+11位手机号
			],
			'user':'tiger'			
		},
]


users=[
	{'name':'user1','user':'tiger','passwd':'111111',
	'sid':'u1'}
]

ao_group=[
	{'name':u'shanghai Traigle Tech.','iconurl':'','user':'tiger','sid':'g1'},
	#{'name':u'上海酷宝信息技术','iconurl':'','user':'user1','sid':'g2'},
	#{'name':u'上海交大汉芯科技','iconurl':'','user':'user1','sid':'g3'},
	#{'name':u'北京神州泰岳技术','iconurl':'','user':'user1','sid':'g4'},
	#{'name':u'上海永生城信技术','iconurl':'','user':'user1','sid':'g5'},
	#{'name':u'上海亚太神通计算机','iconurl':'','user':'user1','sid':'g6'},
	#{'name':u'上海市园林工程公司','iconurl':'','user':'user1','sid':'g7'},
	#{'name':u'英创软件','iconurl':'','user':'user1','sid':'g7'},
	#{'name':u'华东电脑','iconurl':'','user':'user1','sid':'g7'},
	#{'name':u'北京合众思壮','iconurl':'','user':'user1','sid':'g7'},
	#{'name':u'上海联盈数码科技','iconurl':'','user':'user1','sid':'g7'},
	#{'name':u'上海无线通信设备','iconurl':'','user':'user1','sid':'g7'},
]

user_aos={
	'tiger':['K.5H773','F.WP655'],
}

aogroup_aos={
	u'shanghai Traigle Tech.':['K.5H773'],
}



#----------------------------------------------------------------------------#
class DataInitializer:
	def __init__(self):				
		self.rpcAdapter = None
		
		self.services=[]
		self.serviceid='' #das id
		self.GM = None
		self.init()
		
	#初始化配置信息 
	def initConfigs(self):
		
		#django 初始化配置 
		os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
		#sys.path.append(self.config.getValue('django_module_path'))
		self.GM = __import__('giscore.models')  #导入数据库模型

		self.GM = self.GM.models
		
	def init(self):
		try:
			self.initConfigs()

			self.init_data()
		except:
			print traceback.format_exc().decode('utf8')
		


	def dofile(self,name,no):
		print 'dofile:',name
		self.GM.qiyexinxi.objects.filter(fileno=no).delete()
		f = open(name)
		lines = f.readlines()
		f.close()
		for line in lines:
			try:
				line = line.decode('gbk').encode('utf8')
				#print line
				pp = line.strip().split('\t')
				if len(pp) == 9 or len(pp)==7 or len(pp) > 7:
					d = self.GM.qiyexinxi()
					d.name,d.addr,d.zipcode,d.money_s,d.manager,d.tel,d.content = pp[:7]
					d.fileno = no
					d.save()
				if len(pp) == 6:
					d = self.GM.qiyexinxi()
					d.name,d.addr,d.zipcode,d.manager,d.tel,d.content = pp[:6]
					d.fileno = no
					d.save()
			except:
				print 'decode line error!'

	def init_data(self):
		#初始化客户数

		for n in range(5,6):
			self.dofile('d:/qiye/%s.csv'%n,n)

'''
select count(*),fileno  from giscore_qiyexinxi group by fileno  order  by fileno;

'''
		
if __name__=='__main__':
	server = DataInitializer()
	
					
	