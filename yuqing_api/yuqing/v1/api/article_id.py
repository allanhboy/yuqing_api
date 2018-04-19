# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ArticleId(ApiHandler):

    def get(self, id):
        print(id)
        return {}, 200, None