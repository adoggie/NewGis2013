# -- coding:utf-8 --

#uptime_gpsdata.py
#将指定时间范围内的gps记录时间修改为最接近现在的时间

#python uptime_gpsdata.py starttime [hours]
#python uptime_gpsdata.py 20120503  10   5.3日00-10点区间gps记录更新为最近的gps记录
#----------------------------------------------------------------------------#


import socket,traceback,os,os.path,sys,time,struct,base64,gzip,array,threading,json,datetime

from ConfigParser import ConfigParser
from mutex import mutex as Mutex
import string


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
GM = __import__('giscore.models')  #导入数据库模型
GM = GM.models

end = None
start = datetime.datetime.strptime(sys.argv[1],'%Y%m%d')

duration = sys.argv[2:3]
hours = 1
if duration:
	hours = int(duration[0])
	
end = start + datetime.timedelta(hours=hours)

print start,end

dd = GM.AOMData_Gps.objects.filter(savetime__range=(start,end)).order_by('-savetime')
print 'rows:',len(dd)
distance = None
for d in dd:
	if not distance:
		distance = datetime.datetime.now() - d.savetime
	d.savetime = d.savetime + distance
	d.save()


