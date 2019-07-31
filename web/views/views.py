#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time         : 2018/12/27 11:15
# @Author       : lihongwei@integritytech.com.cn
# @Site         : 
# @File         : views.py
# @Software     : PyCharm

import tornado.web
from ..session import Session


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = Session(self)
        super(BaseHandler, self).initialize()


class AuthHandler(BaseHandler):

    def prepare(self):
        print "登陆验证"
        if not self.session.get("is_login"):
            self.redirect("/login")
        else:
            super(AuthHandler, self).prepare()


class PermissionHandler(BaseHandler):

    def prepare(self):
        print "权限验证"
        if not self.session.get("permission"):
            self.redirect("/login")
        else:
            super(PermissionHandler, self).prepare()


class MainHandler(AuthHandler, PermissionHandler):
    def get(self):
        render_dict = {"k1": [123, 234],
                       "k2": {"name": "lihongwei"}}
        self.render("index.html", **render_dict)

    def post(self):
        self.write("ok")


class LoginHandler(BaseHandler):

    def get(self):
        self.render("login.html")

    def post(self, *args, **kwargs):
        request_dict = dict()
        for k, v in self.request.arguments.items():
            request_dict[k] = v[-1]
        if request_dict["username"] == "lihongwei549@163.com" and request_dict["password"] == "123":
            self.session.set("is_login", True)
            self.session.set("permission", dict(k=1))
            self.redirect("/index")
        else:
            self.redirect("/login")

