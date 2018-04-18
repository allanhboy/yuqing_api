# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from core import PackageDB,PackageSession
import hashlib  ##MD5加密

class AccountLogin(ApiHandler):

    def post(self):
        dbsession = PackageDB._connectDBdata_()
        username = self.json['username']
        password = self.json['password']
        if username and password:
            dbpassword=dbsession.query(PackageDB.employee.password).filter_by(username=username).first()
            if dbpassword:
                passwordmd5 = hashlib.md5()   
                passwordmd5.update(password.encode(encoding='utf-8'))
                if dbpassword[0] == passwordmd5.hexdigest():
                    session = PackageSession.Session(self,1)    
                    session['username'] = username                    
                    session['password'] = password                    
                    session['loginstatus'] = True
                    return None, 204, None
                else:
                    return  None, 400, None
            else:
                return  None, 400, None
        else:
            return  None, 400, None