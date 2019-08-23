#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time         : 2018/12/27 12:58
# @Author       : lihongwei@integritytech.com.cn
# @Site         : 
# @File         : uimodules.py
# @Software     : PyCharm

from tornado.web import UIModule
from tornado import escape


class custom(UIModule):

    def render(self, *args, **kwargs):
        return escape.xhtml_escape('<h1>wupeiqi</h1>')
