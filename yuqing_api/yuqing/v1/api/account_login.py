# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from core.PackageDB import employee,_connectDBdata_
import hashlib  ##MD5加密

class AccountLogin(ApiHandler):

    def post(self):
        user = self.get_current_user()
        if user.valid:
            dbsession = _connectDBdata_()
            username = self.json['username']
            password = self.json['password']
            #判断账户密码是否输入
            if username and password:
                dbemployee=dbsession.query(employee).filter_by(username=username).first()
                #判断账号是否存在
                if dbemployee.password:
                    passwordmd5 = hashlib.md5()   
                    passwordmd5.update(password.encode(encoding='utf-8'))
                    #判断密码正确性
                    if dbemployee.password == passwordmd5.hexdigest():
                        #判断employee是否已绑定openid
                        if dbemployee.openid is None:
                            dbemployee.session_key =user.session.session_key
                            dbemployee.openid = user.session.openid
                            dbsession.add(dbemployee)
                            dbsession.commit()
                            return  None, 204, None
                        else:
                             #判断openid是否一致
                            if dbemployee.openid == user.session.openid:
                                dbemployee.session_key =user.session.session_key
                                dbemployee.openid = user.session.openid
                                dbsession.add(dbemployee)
                                dbsession.commit()
                                return  None, 204, None
                            else:
                                return  {"code":0,"message":"账号已绑定其他微信"}}, 400, None
                    else:
                        return  {"code":0,"message":"密码错误"}}, 400, None
                else:
                    return  {"code":0,"message":"账号不存在"}}, 400, None
            else:
                return  {"code":0,"message":"请输入账号或者密码"}}, 400, None
        else:
            return  {"code":0,"message":"未找到微信信息"}}, 400, None