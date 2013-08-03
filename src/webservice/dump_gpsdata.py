# -- coding:utf-8 --

#dump_gpsdata.py 
#转储gps数据
#----------------------------------------------------------------------------#


import socket,traceback,os,os.path,sys,time,struct,base64,gzip,array,threading,json

from ConfigParser import ConfigParser
from mutex import mutex as Mutex
import string


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
GM = __import__('giscore.models')  #导入数据库模型
GM = GM.models
		
gps = GM.AO_ModuleLog.objects.filter(type=2)

fp = open('gpslog.txt','w')
for d in gps:
	fp.write(d.rawmsg)
	fp.write('\n')
fp.close()
print 'dumping okay!'
					
	