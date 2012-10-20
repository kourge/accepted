#!/usr/bin/env python
import web

import auth
import controller
from profilecontroller import ProfileController
from resumecontroller import ResumeController
from creatorcontroller import CreatorController


urls = (
    r'/login', 'login',
    r'/logout', 'logout',
    r'/creator', 'CreatorController',
    r'/profile', 'ProfileController',
    r'/resume', 'ResumeController',
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
