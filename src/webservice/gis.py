# -*- coding:utf-8 -*-
#comments line
#----------------------------------------------------------------------------#

import sys,os
import traceback,threading,time,struct,os,os.path,shutil,distutils.dir_util,array,base64,zlib,struct,binascii
import datetime
import json
from django.http import *
from django.shortcuts import render_to_response
#from giscore.models import *
import giscore.models

JSLIB_PATH='http://192.168.14.66:9000'
JSLIB_PATH='http://wallizard.vicp.net/maps/js'
JSLIB_OPENLAYERS=JSLIB_PATH+'/OpenLayers-2.8'
JSLIB_GEOEXT=JSLIB_PATH+'/GeoExt'
JSLIB_EXTJS=JSLIB_PATH+'/ext'
JSLIB_GIS='/medias/js/gis' #存放gis系统的js目录 

def mainWindow(request):
    return render_to_response('mainwindow.html',
                              {'jslib_path':JSLIB_PATH,
                               'jslib_openlayers':JSLIB_OPENLAYERS,
                               'jslib_geoext':JSLIB_GEOEXT,
                               'jslib_extjs':JSLIB_EXTJS,
                               'jslib_gis':JSLIB_GIS,
                               })



def getPosObjects(request):
    treeNodes=[
        {'id':2,'text': 'Menu Option 2','leaf': True,'checked':False},
        {'id':1000,'text': '设备1','hwid':'A-1002'
            ,'children':[
                {'id':1002,'text': '设备1','leaf': True,'checked':False,'hwid':'A-1002'}
            ]
        },
        {'id':100,'text': '设备1','leaf': True,'checked':False,'hwid':'A-1002'},
        
        {'id':3,'text': 'Menu Option 3','leaf': True,'checked':False},
    ]		
    datas = json.dumps(treeNodes)
    print datas,'12'*10
    return HttpResponse(datas)

#----------------------------------------------------------------------------#
'''
@params:
    {'userid',}
@returns:
    [{'id','text','leaf','checked','children'},]
'''
#----------------------------------------------------------------------------#
def getActiveObjects(req):
    rs = []
    userid = 'user1' #params['userid']
    grps = giscore.models.AO_Group.objects.filter(user__name=userid)

    for g in grps:
        r1={}
        r1['id'] = g.id
        r1['text'] = g.name
        #r1['checked'] =False
        r1['children']=[]
        aos = g.aos
        for ao in aos.all():
          r2={}
          r2['id'] = ao.id
          r2['text'] = ao.name
          r2['leaf'] = True
          r2['iconCls'] ='aoIcon'
          r1['children'].append(r2)
          
        rs.append(r1)
    rs = json.dumps(rs)
    print '-*'*20
    print rs
    return HttpResponse(rs)

#----------------------------------------------------------------------------#
'''
@params: Array
    [ ['aoid','lasttime'],]
    系统对象编号,上一次获取gps数据的时间
    如果时间相同则无需返回gps数据. lasttime(timestamp)
@returns: Array
    {'result':[{'aoid','time','satenum','sateused','lon','lat','speed','angle'},])
'''
# time.mktime(datetime.datetime.now().timetuple())
#----------------------------------------------------------------------------#
def getGpsData(request):
    
    aos = json.loads(request.POST['params'])
    rst=[]
    print aos
    for ao in aos:
        aoid,lasttime = map(int,ao[:2])        
        dt = datetime.datetime.fromtimestamp(lasttime)
        
        #按时间降序，最近一条记录且时间大于上一次读取的数据(减少负荷和流量)        
        rs = giscore.models.AOMData_Gps.objects.filter(savetime__gt=dt,aom__ao__id=aoid).order_by('-savetime')[0:1]        
        if rs:
            r = rs[0]
            e ={}
            e['aoid'] = aoid
            ts = time.mktime(r.savetime.timetuple())
            e['time'] = int(ts)
            e['satenum'] = r.satenum
            e['sateused'] = r.sateused
            e['lon'] = r.lon
            e['lat'] = r.lat
            e['speed'] = r.speed
            e['angle'] = r.angle
            rst.append(e)
    rst = json.dumps({'result':rst})
    print rst
    return HttpResponse(rst)

#----------------------------------------------------------------------------#
'''
    {'aoid','starttime','endtime'} start&end is timestamp 
@returns:
    {'aoid','traces':[{'time','satenum','sateused','lon','lat','speed','angle'}]}
'''
#----------------------------------------------------------------------------#
def getGpsDataByTimeRange(req):
    pass
#----------------------------------------------------------------------------#

