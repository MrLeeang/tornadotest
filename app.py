#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time         : 2018/12/27 15:46
# @Author       : lihongwei@integritytech.com.cn
# @Site         : 
# @File         : app.py
# @Software     : PyCharm

from web import application
import tornado.ioloop
import tornado.httpserver


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
