#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:wefinger
from tornado import web,httpserver,ioloop
import time,datetime
import re

class MainHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

class sendHandler(web.RequestHandler):
    def post(self, *args, **kwargs):
        mesg = self.get_argument('query')
        check_zh = re.compile(u'[\u4e00-\u9fa5]+')
        match = check_zh.search(mesg)
        if mesg != "":
            if match:
                self.render('error.html',info=['发送字符中含有中文！请重新发送！'])
            else:
                with open("mes.log", "a") as f:
                    f.write(mesg)
                    f.write('\n')
                self.render('ok.html')
        else:
            self.render('error.html',info=['内容为空！请返回重新发送'])

class testHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('test.html')

class shuaxinHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        t = str(datetime.datetime.now())
        self.write(t)

if __name__ == "__main__":
    application = web.Application([
        (r"/", MainHandler),
        (r"/query", sendHandler),
        (r"/test", testHandler),
        (r"/shuaxin", shuaxinHandler),
    ])
    application.listen(82) #监听端口号
    ioloop.IOLoop.current().start()