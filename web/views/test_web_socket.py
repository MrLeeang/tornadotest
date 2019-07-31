#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time         : 2019/3/21 11:45
# @Author       : lihongwei@integritytech.com.cn
# @Site         : 
# @File         : test_web_socket.py
# @Software     : PyCharm


import tornado.web
import tornado.websocket
import tornado.ioloop


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.write_message(u"连接成功，%s" % self.get_argument('name'))

    def on_message(self, message):
        self.write_message(u"Your message was: " + message)

    def on_close(self):
        pass


class IndexPageHandler(tornado.web.RequestHandler):
    def get(self):

        import time
        time.sleep(20)
        self.render("websockets.html")
