# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import json
import urllib.request
import uuid
from datetime import datetime, timedelta

from core.PackageDB import _connectDBdata_, employee, session
from core.webconfig import appid,appscred

from . import ApiHandler
from .. import schemas

class WechatLogin(ApiHandler):
    def post(self):
        code = self.json['code']
        random = self.json['random']
        # 获取微信opneid等信息
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={APPID}&secret={SECRET}&js_code={JSCODE}&grant_type=authorization_code'.format(
            APPID=appid, SECRET=appscred, JSCODE=code)
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
        the_page_utf_8 = the_page.decode('utf-8')
        weixininfo = json.loads(the_page_utf_8)
        if weixininfo.get('openid') is None:
            return {'code': 400, 'message': 'code 无效'}, 400, None

        session_key = weixininfo['session_key']
        openid = weixininfo['openid']
        unionid = weixininfo.get('unionid', None)

        # #微信信息插入session表
        respone = {}
        id = uuid.uuid1()
        expiretime = datetime.now()+timedelta(days=7)
        sessioninfo = session(id=str(id), openid=openid, session_key=session_key,
                              random=random, expire_time=expiretime, unionid=unionid)
        respone['session'] = sessioninfo.id
        respone['expire_time'] = sessioninfo.expire_time.strftime(
            '%Y/%m/%d %H:%M:%S')

        #判断employee是否绑定openid,绑定给session的employee赋值
        dbsession = _connectDBdata_()
        dbemployeeid = dbsession.query(employee.id).filter_by(openid=openid).one_or_none()
        if dbemployeeid:
            sessioninfo.employee_id = dbemployeeid[0]
            respone['is_binding'] = 1
        else:
            respone['is_binding'] = 0
        dbsession.add(sessioninfo)
        dbsession.commit()
        dbsession.close()
        return respone, 200, None
