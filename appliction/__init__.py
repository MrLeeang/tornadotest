#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time         : 2018/12/27 15:44
# @Author       : lihongwei@integritytech.com.cn
# @Site         : 
# @File         : __init__.py.py
# @Software     : PyCharm

import tornado.web
from appliction import uimethods
from appliction import uimodules

from appliction.views.views import MainHandler
from appliction.views.views import LoginHandler
from appliction.views.views import TestAwaitHandler
from appliction.views.test_web_socket import WebSocketHandler, IndexPageHandler
from appliction.views.chat import ChatHome, chatBasicHandler, homeHandler, newChatStatus

settings = {
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'template_path': 'templates',
    'ui_methods': uimethods,
    'ui_modules': uimodules,
}

application = tornado.web.Application([
    (r"/", IndexPageHandler),
    (r"/test", TestAwaitHandler),
    (r"/index", MainHandler),
    (r"/login", LoginHandler),
    (r"/ws", WebSocketHandler),
    (r'/chat', chatBasicHandler),
    (r'/chat/home/', homeHandler),
    (r'/chat/newChatStatus/', newChatStatus),
], **settings)
application.chathome = ChatHome()
# application.add_handlers()
