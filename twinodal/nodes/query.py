#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nodal.nodes import BaseNode
from twicorder.queries import ProductionRequestQuery


class QueryNode(BaseNode):

    _output_type = {'default': [], 'type': list}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._query = ProductionRequestQuery(*args, **kwargs)

    @property
    def query(self):
        return self._query

    def _execute(self):
        while not self.query.done:
            result = self.query.start()
            self._result += result
            yield result
