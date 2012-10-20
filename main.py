#!/usr/bin/env python
import web

import auth
import controller
from profilecontroller import ProfileController
from resumecontroller import ResumeController


urls = (
    r'/login', 'login',
    r'/logout', 'logout',
    r'/profile', 'ProfileController',
    r'/resume', 'ResumeController',
    r'/', 'index',
)


class IndexController(controller.Controller):
    pass


class login(object):
    def GET(self):
        return auth.login(web.ctx.env.get('HTTP_REFERER'))


class logout(object):
    def GET(self):
        return auth.logout('/')


app = web.application(urls, globals()).wsgifunc()
