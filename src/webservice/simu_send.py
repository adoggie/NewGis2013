#--coding:utf-8--
#模拟ks168连接到dtuserver，发送BP05消息
#读取gps
import socket,traceback,os,os.path,sys,time,struct,base64,gzip,array,json,zlib,threading,select


data='''(013661940344BP05000013661940344120420A3110.4246N12123.3105E000.0115439182.0500000000L000E3B8E)'''

s =socket.socket()
s.connect(("61.152.116.120",58663))
for n in range(100):
	s.sendall(data*1)
	time.sleep(1)
	
s.close()
