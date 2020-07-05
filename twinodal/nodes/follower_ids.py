#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nodal.nodes import BaseNode
from twicorder.queries.request_queries import FollowerIDQuery


class FollowerIDNode(BaseNode):

    _input_types = {
        0: {'name': 'user_id', 'types': [int], 'default': None},
        1: {'name': 'screen_name', 'types': [str], 'default': None}
    }
    _output_type = {'default': [], 'type': list}
    _max_inputs = 1

    def _execute(self):
        query = FollowerIDQuery()