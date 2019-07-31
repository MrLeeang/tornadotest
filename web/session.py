#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time         : 2018/12/27 13:55
# @Author       : lihongwei@integritytech.com.cn
# @Site         : 
# @File         : session.py
# @Software     : PyCharm

import uuid


container = {}


class Session(object):

    def __init__(self, handler):
        self.handler = handler

        self.session_id = self.handler.get_cookie("session_id")

        if not self.session_id:
            self.session_id = str(uuid.uuid4())
            self.handler.set_cookie("session_id", self.session_id)

        if not container.get(self.session_id):
            container[self.session_id] = dict()

        self.session_dict = container[self.session_id]
        self.set("timeout", 1000)

    def get(self, key):
        return self.session_dict.get(key)

    def set(self, key, value):
        self.session_dict[key] = value
        return True

    def remove(self, key):
        return self.session_dict.pop(key)

    def destroy(self):
        return container.pop(self.session_id)
