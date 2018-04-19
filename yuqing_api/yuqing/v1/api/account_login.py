# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from core import PackageDB,PackageSession
import hashlib  ##MD5加密

class AccountLogin(ApiHandler):

    def post(self):
        user = self.get_current_user()
        if user.valid:
            dbsession = PackageDB._connectDBdata_()
            username = self.json['username']
            password = self.json['password']
            if username and password:
                dbemployee=dbsession.query(PackageDB.employee).filter_by(username=username).first()
                if dbemployee.password:
                    passwordmd5 = hashlib.md5()   
                    passwordmd5.update(password.encode(encoding='utf-8'))
                    if dbemployee.password == passwordmd5.hexdigest():
                        if dbemployee.openid is None:
                            dbemployee.session_key =user.session.session_key
                            dbemployee.openid = user.session.openid
                            dbsession.add(dbemployee)
                            dbsession.commit()
                            return  None, 204, None
                        else:
                            if dbemployee.openid == user.session.openid:
                                dbemployee.session_key =user.session.session_key
                                dbemployee.openid = user.session.openid
                                dbsession.add(dbemployee)
                                dbsession.commit()
                                return  None, 204, None
                            else:
                                return  None, 400, None
                    else:
                        return  None, 400, None
                else:
                    return  None, 400, None
            else:
                return  None, 400, None
        else:
            return  None, 400, None
        return  None, 400, None