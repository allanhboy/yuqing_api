# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Articles(ApiHandler):

    def get(self):
        page_index = self.args['page_index']
        follow_type = self.args['follow_type']
        user = self.get_current_user()
        if user.valid:
            print('111')
        return {}, 200, None