# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from core.PackageDB import session,employee,_connectDBdata_
import urllib.request
import json
import uuid
from datetime import datetime, timedelta


class WechatLogin(ApiHandler):

    def post(self):
        dbsession = _connectDBdata_()
        dbsession.query(employee).all()
        code = self.json['code']
        random =  self.json['random']
        appid = 'wx1154d8019b1db191'
        appscred = '12d3e5086ac152c27e6d2cd30966b326'
        #获取微信opneid等信息
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code'.format(APPID=appid,SECRET=appscred,JSCODE=code)
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        the_page_utf_8 = the_page.decode('utf-8')
        weixininfo = json.loads(the_page_utf_8)
        if weixininfo.get('openid') is None:
           return {'code':400,'message':'code 无效'},400,None

        session_key = weixininfo['session_key']
        openid = weixininfo['openid']

        # #微信信息插入session表
        respone = {}
        id = uuid.uuid1()
        expiretime=datetime.now()+timedelta(days=7)
        sessioninfo = session(id=str(id),openid=openid,session_key=session_key,random=random,expire_time=expiretime)
        respone['session'] = sessioninfo.id
        respone['expire_time'] = sessioninfo.expire_time.strftime('%Y/%m/%d %H:%M:%S')

        # #判断employee是否绑定openid,绑定给session的employee赋值
        dbemployeeid = dbsession.query(employee.id).filter_by(openid=openid).one_or_none()
        if dbemployeeid:       
            sessioninfo.employee_id = dbemployeeid[0]
            dbsession.add(sessioninfo)
            dbsession.commit()
            respone['is_binding'] = 1
            dbsession.close()
            return respone,200, None
        else:
            respone['is_binding'] = 0
            dbsession.add(sessioninfo)
            dbsession.commit()
            dbsession.close()
            return respone, 200, None