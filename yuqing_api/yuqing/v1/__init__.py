# -*- coding: utf-8 -*-
from __future__ import absolute_import

from core import PackageDB,PackageSession
from core.PackageDB import session, employee 

class UserInfo(object):
    _scopes = None
    client_id = None
    _session = None
    _employee = None

    def __init__(self, session_id, authorization, blueprint):
        self.authorization = authorization
        self.session_id = session_id
        self.blueprint = blueprint
        with PackageDB._connectDBdata_() as dbsession:
            self.valid = dbsession.query(session).filter(session.id == session_id).count() > 0

    @property
    def scopes(self):
        if self._scopes is None:
            self._scopes = self._loader()
        return self._scopes

    def _loader(self):
        return []

    @property
    def session(self):
        if self._session is None:
            if self.valid and self.session_id:
                # TODO: test
                with PackageDB._connectDBdata_() as dbsession:
                    self._session = dbsession.query(session).filter(session.id == self.session_id).one()
                
        return self._session

    @property
    def employee(self):
        if self._employee is None:
            if self.valid:
                sess =  self.session
                if sess:
                     with PackageDB._connectDBdata_() as dbsession:
                         self._employee = dbsession.query(employee).filter(employee.id == sess.employee_id).one_or_none()

        return self._employee