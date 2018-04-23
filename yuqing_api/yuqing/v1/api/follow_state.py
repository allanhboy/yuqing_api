# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from . import ApiHandler
from .. import schemas


class FollowState(ApiHandler):

    def get(self):

        return {}, 200, None