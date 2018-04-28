# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import hashlib  # MD5加密

from core.PackageDB import _connectDBdata_, employee

from . import ApiHandler
from .. import schemas


class AccountLogin(ApiHandler):
    def post(self):
        user = self.get_current_user()
        if not user.valid:
            return {"code": 0, "message": "未登录"}, 401, None

        username = self.json['username']
        password = self.json['password']
        # 判断账户密码是否输入
        if username and password:
            dbsession = _connectDBdata_()
            try:
                dbemployee = dbsession.query(employee).filter_by(
                    username=username).one_or_none()
                # 判断账号是否存在
                if dbemployee and dbemployee.password:
                    passwordmd5 = hashlib.md5()
                    passwordmd5.update(password.encode(encoding='utf-8'))
                    # 判断密码正确性
                    if dbemployee.password == passwordmd5.hexdigest().upper():
                        # 判断employee是否已绑定openid，否则执行绑定操作
                        if dbemployee.openid is not None and dbemployee.openid != user.session.openid:
                            return {"code": 400, "message": "账号已绑定其他微信"}, 400, None
                        dbemployee.session_key = user.session.session_key
                        dbemployee.openid = user.session.openid
                        dbemployee.unionid = user.session.unionid
                        dbsession.add(dbemployee)
                        user.session.employee_id = dbemployee.id
                        dbsession.add(user.session)
                        dbsession.commit()
                        return None, 204, None
                    else:
                        return {"code": 400, "message": "密码错误"}, 400, None
                else:
                    return {"code": 400, "message": "账号不存在"}, 400, None
            except:
                return {"code": 400, "message": "登录失败，请刷新重试"}, 400, None
            finally:
                dbsession.close()
        else:
            return {"code": 400, "message": "请输入账号或者密码"}, 400, None
