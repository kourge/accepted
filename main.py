#!/usr/bin/env python
import web


urls = (
    r'/.*', 'Hello',
)


class Hello(object):
    def GET(self):
        return 'Herro, world!'


app = web.application(urls, globals()).wsgifunc()
