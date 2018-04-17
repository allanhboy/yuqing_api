# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class ArticleIdInvalid(ApiHandler):

    def put(self, id):

        return None, 204, None