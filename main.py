#!/usr/bin/env python
import web

import auth
import controller
from profilecontroller import ProfileController
from resumecontroller import ResumeController, ResumeGenerationController
from exportcontroller import ExportController


urls = (
    r'/login', 'login',
    r'/logout', 'logout',
    r'/profile', 'ProfileController',
    r'/resume', 'ResumeController',
    r'/resume/create', 'ResumeGenerationController',
    r'/export/(.+)', 'ExportController',
    r'/', 'IndexController',
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
