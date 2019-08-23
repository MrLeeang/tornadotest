#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time         : 2019/8/23 15:14
# @Author       : Li Hongwei
# @Email        : lihongwei@integritytech.com.cn
# @File         : flaskapp.py
# @Software     : PyCharm

from flask import Flask
from gevent import monkey
from gevent.pywsgi import WSGIServer
monkey.patch_all()


appliction = Flask(__name__)
appliction.config.update(DEBUG=True)


@appliction.route("/")
def index():
    import time
    time.sleep(100)
    return "fd"


@appliction.route("/test")
def test():

    return "test"


if __name__ == "__main__":
    # appliction.run()
    http_server = WSGIServer(('', 5000), appliction)
    http_server.serve_forever()
