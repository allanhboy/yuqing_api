# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas

from core import PackageDB,PackageSession

class Home(ApiHandler):

    def get(self):
        session = PackageSession.Session(self,1)    
        username=session['username']
        print(username)               

        return {}, 200, None