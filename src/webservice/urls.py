from django.conf.urls.defaults import *
import os,sys


MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'medias').replace('\\','/')

print MEDIA_ROOT

urlpatterns = patterns('',
		(r'^medias/(?P<path>.*)$', 'django.views.static.serve',{'document_root': MEDIA_ROOT}),
		
		(r'^$', 'gis.mainWindow'), 		
		(r'^getGpsData', 'gis.getGpsData'),
		(r'^getActiveObjects/','gis.getActiveObjects'),
		(r'^getGpsDataByTimeRange/','gis.getGpsDataByTimeRange'),
		(r'^gateway/$', 'amfgateway.gateway'),
)
