#--coding:utf-8--

#from gevent import monkey ; monkey.patch_all()
from gevent.wsgi import WSGIServer
import sys
import os
import traceback
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import call_command
from django.core.signals import got_request_exception

sys.path.insert(0,'../../tce/python')
sys.path.insert(0,'../')

import tcelib as tce
import newgis
import utils

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

tce.RpcCommunicator.instance().init('webserver_1','../services.xml')

def exception_printer(sender, **kwargs):
	traceback.print_exc()

got_request_exception.connect(exception_printer)
#call_command('syncdb')

appname = 'webserver'
utils.app_kill(appname)
utils.app_init(appname)

PORT   = 8088
if len(sys.argv) > 1:
	PORT = int(sys.argv[1])
print 'Serving on %s...'%PORT
WSGIServer(('', PORT), WSGIHandler()).serve_forever()
