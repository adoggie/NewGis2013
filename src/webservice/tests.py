# -*- coding:utf-8 -*-

 
import sys,os
import traceback,threading,time,struct,os,os.path,shutil,distutils.dir_util,array,base64,zlib,struct,binascii


from django.http import *
from django.shortcuts import render_to_response
import json
def hello(r):
    print r
    return HttpResponse('that is ok')

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