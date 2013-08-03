# -*- coding:utf-8 -*-
#导入ip网段库记录

import sys,os

import traceback,threading,time,struct,os,os.path,zlib,struct,string
import psycopg2

#import log,config

'''

CREATE DATABASE IpRedirect
  WITH OWNER = postgres
       ENCODING = 'UTF8';

CREATE TABLE IpRepository
(
  
  startip bigint NOT NULL,
	endip bigint NOT NULL,
  name character varying(40) NOT NULL
)
WITH (OIDS=TRUE);
ALTER TABLE IpRepository OWNER TO postgres;




'''



#function Paging(total) {
#	this.pageSize = 10;//每页显示记录数
#	this.step = 5;//最多显示分页页数
#	this.total = total; //总记录数
#}


g_dbconn = None


def getDBConn():
	global g_dbconn
	try:
		if g_dbconn == None:
			dbhost='localhost'
			dbname='newgps'
			dbuser='postgres'
			dbpasswd='111111'
			g_dbconn = psycopg2.connect(host=dbhost,database=dbname,user=dbuser,password=dbpasswd)
	except:
		traceback.print_exc()
	return g_dbconn
	

def importIpTables():
	fp = open('ipdata/ipdata.txt')
	lines = fp.readlines()
	#print len(lines)
	fp.close()
	conn = getDBConn()
	cr = conn.cursor()
	print 'size:',len(lines)
	cc=0
	for line in lines:
		parts=None
		try:
			if cc%1000==0:
				print cc
			cc+=1
			parts = line.strip().split('_')
			parts = map(string.strip,parts)
			if len(parts) <3:
				continue
			#insert ip table by sql statements
			sql = "insert into IpRepository values(%s,%s,%s);"
			
			
			#print parts
			#print parts[0],parts[1]
			cr.execute(sql,(long(parts[0]),long(parts[1]),parts[2].decode('utf8'),))
			conn.commit() 
		except:
			traceback.print_exc()
			#cr = conn.cursor()
			#g_logger.error(traceback.format_exc())
			#print parts
			return 
	
		
		

if __name__=='__main__':
	importIpTables()
	#server = sepApp()
	#sys.exit(server.run())
	
	
		
	