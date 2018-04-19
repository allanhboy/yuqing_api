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
        code = self.json['code']
        random =  self.json['random']
        appid = 'wx1154d8019b1db191'
        appscred = '12d3e5086ac152c27e6d2cd30966b326'
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code'.format(APPID=appid,SECRET=appscred,JSCODE=code)
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        the_page_utf_8 = the_page.decode(encoding="utf-8")
        weixininfo = json.loads(the_page_utf_8)
        session_key = weixininfo['session_key']
        openid = weixininfo['openid']

        respone = {}
        id = uuid.uuid1()
        expiretime=datetime.now()+timedelta(days=7)
        sessioninfo = session(id=id,openid=openid,session_key=session_key,random=random,expire_time=expiretime)
        dbsession.add(sessioninfo)
        dbsession.commit()
        respone['session'] = sessioninfo.id
        respone['expire_time'] = sessioninfo.expire_time.strftime('%Y-%m-%d %H:%M:%S') 

        dbemployeeid = dbsession.query(employee.id).filter_by(openid=openid).first()
        if dbemployeeid:
            dbsessioninfo = dbsession.query(session).filter_by(openid=openid).order_by(session.create_time.desc()).first()
            dbsessioninfo.employee_id = dbemployeeid
            dbsession.add(dbsessioninfo)
            dbsession.commit()
            respone['is_binding'] = 1
            return respone, 200, None
        else:
            respone['is_binding'] = 0
            return respone, 403, None