# -*- coding:utf-8 -*-

import pyamf
from pyamf.flex import ArrayCollection, ObjectProxy
from pyamf.remoting.gateway.django import DjangoGateway
#from giscore.models import AO_Group
import gisserver
import gisadmin


#pyamf.register_class(AO_Group, 'com.subscription.vos.SubscriberVO')

print 'init amfgateway...'
a = gisadmin.GisAdmin.instance()
s = gisserver.GisServer.instance()
print a,s

#print m,a
services = {

	'gis.doLogin':s.doLogin,
	'gis.doLogout':s.doLogout,
	#'gis.getServerTime':s.getServerTime,
	'gis.getActiveObjectList':s.getActiveObjectList,
	'gis.getActiveObjectListWithGroup':s.getActiveObjectListWithGroup,			#获取所有ao对象,已分组
	'gis.queryActiveObjectByName':s.queryActiveObjectByName,	#根据名称获取ao对象列表
	'gis.queryVisitedPointList':s.queryVisitedPointList,
	'gis.createVisitedPoint':s.createVisitedPoint,
	'gis.updateVisitedPoint':s.updateVisitedPoint,
	'gis.deleteVisitedPoint':s.deleteVisitedPoint,
	#'gis.ctrl.'
	'gis.getActiveObjectInfo':s.getActiveObjectInfo,	#查询ao对象信息
	
	'gis.getSystemParameter':s.getSystemParameter,
	'gis.getSystemParamList':s.getSystemParamList,
	'gis.getAoTrackPathNearestTime':s.getAoTrackPathNearestTime,
	'gis.getActiveObjectListByName':s.getActiveObjectListByName,
	'gis.getAoReplayTrackData':s.getAoReplayTrackData,
	'gis.gisGeoObjectQuery':s.gisGeoObjectQuery,
	'gis.convertXy_g2m':s.convertXy_g2m,



    'gis.getUserInfo':s.getUserInfo,
    'gis.updateUserInfo':s.updateUserInfo,


	'gis.queryUserLoginList':s.queryUserLoginList,


	'gis.getIdentifyCodeImage':s.getIdentifyCodeImage,


    #2012.5.24 add usermessage apis
    'gis.getUserMessageList':s.getUserMessageList,
    'gis.createUserMessage':s.createUserMessage,
    'gis.deleteUserMessage':s.deleteUserMessage,
    'gis.replyUserMessage':s.replyUserMessage,#系统管理员回复用户消息

    'gis.getAoReport_Miles':s.getAoReport_Miles,

    'gis.ctrlset_reset':s.ctrlset_reset,
    'gis.ctrlset_startListen':s.ctrlset_startListen,
	'gis.ctrlset_clearMiles':s.ctrlset_clearMiles,



	'gis.deleteBarrier':s.deleteBarrier,
    'gis.updateBarrier':s.updateBarrier,
    'gis.createBarrier':s.createBarrier,
	'gis.getBarrier':s.getBarrier,
	'gis.getBarrierList':s.getBarrierList,

	'gis.attachAsi':s.attachAsi,
    'gis.detachAsi':s.detachAsi,
    'gis.getAsiListOfAo':s.getAsiListOfAo,

    'gis.createAsi':s.createAsi,
    'gis.deleteAsi':s.deleteAsi,
    'gis.updateAsi':s.updateAsi,
    'gis.getAsiList':s.getAsiList,
    'gis.getAsiInfo':s.getAsiInfo,

    'gis.getAoReport_AlarmActions':s.getAoReport_AlarmActions,
    'gis.getAoReport_AlarmLogs':s.getAoReport_AlarmLogs,

    'gis.getNoticeItem':s.getNoticeItem, #获取通告
	'gis.getUserParams':s.getUserParams,
	'gis.setUserParams':s.setUserParams,

    'admin.getNoticeList':a.getNoticeList,
    'admin.createNoticeItem':a.createNoticeItem,
    'admin.updateNoticeItem':a.updateNoticeItem,
	'admin.deleteNoticeItem':a.deleteNoticeItem, #删除通告




	'admin.getUserList':a.getUserList,
	'admin.getUserAoGroups':a.getUserAoGroups,
	'admin.getActiveObjectListOfUser':a.getActiveObjectListOfUser,
	'admin.getActiveObjectListOfUserGroup':a.getActiveObjectListOfUserGroup,
	'admin.getActiveObjectList':a.getActiveObjectList,

	'admin.removeAoFromUser':a.removeAoFromUser,
	'admin.addAoIntoUser':a.addAoIntoUser,

	'admin.removeAoFromUserGroup':a.removeAoFromUserGroup,
	'admin.addAoIntoUserGroup':a.addAoIntoUserGroup,

    'admin.createAoUserGroup':a.createAoUserGroup,
    'admin.deleteAoUserGroup':a.deleteAoUserGroup,
	'admin.updateAoUserGroup':a.updateAoUserGroup,
	'admin.getUserAoGroupDetail':a.getUserAoGroupDetail,



	#系统设备组
    'admin.getAoSysGroupDetail':a.getAoSysGroupDetail,
	'admin.updateAoSysGroup':a.updateAoSysGroup,
	'admin.createAoSysGroup':a.createAoSysGroup,

	'admin.deleteAoSysGroup':a.deleteAoSysGroup,
	'admin.addAoIntoSysGroup':a.addAoIntoSysGroup,
	'admin.removeAoFromSysGroup':a.removeAoFromSysGroup,
	'admin.getAoSysGroupList':a.getAoSysGroupList,
	'admin.getAoListOfSysGroup':a.getAoListOfSysGroup,
	
	'admin.createUser':a.createUser,
	'admin.updateUser':a.updateUser,
	'admin.deleteUser':a.deleteUser,

	'admin.getUserDetail':a.getUserDetail,


	'admin.createActiveObject':a.createActiveObject,
	'admin.updateActiveObject':a.updateActiveObject,
	'admin.deleteActiveObject':a.deleteActiveObject,
	'admin.getActiveObjectInfo':a.getActiveObjectDetail,

	'admin.queryLoginList':a.queryLoginList,
    'admin.login':a.login,
	'admin.logout':a.logout,

	'admin.getSysParamList':a.getSysParamList,
    'admin.getSysParamInfo':a.getSysParamInfo,
    'admin.createSysParam':a.createSysParam,
    'admin.updateSysParam':a.updateSysParam,
    'admin.deleteSysParam':a.deleteSysParam,

    'admin.getAoNearestGpsData':a.getAoNearestGpsData,


    'admin.getUserMessageList':a.getUserMessageList,
    'admin.deleteUserMessage':a.deleteUserMessage,
    'admin.replyUserMessage':a.replyUserMessage,#

}

gateway = DjangoGateway(services, expose_request=True)
