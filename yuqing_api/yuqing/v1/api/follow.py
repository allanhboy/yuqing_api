# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class Follow(ApiHandler):

    def post(self):
        print(self.json)

        return None, 204, None

    def delete(self):
        print(self.json)

        return None, 204, None