#--coding:utf-8--


import os,os.path,sys,struct,time,traceback,signal,threading

CONF = os.getenv('SNS_CONFIG')
path = os.path.dirname(CONF)
sys.path.insert(0,path)
from sns_init import *

from snsbase.base import *



#print dir(snsbase.base)

