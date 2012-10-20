#!/usr/bin/env python
import web
import os
import jinja2
from google.appengine.api import users

from models import *
import auth

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

urls = (
    r'/login', 'login',
    r'/logout', 'logout',
    r'/profile', 'profile',
    r'/resume', 'resume',
    r'/', 'index',
)

class renderer(object):
    def GET(self):
        return jinja_environment.get_template(
            'templates/%s.html' % (self.__class__.__name__,)
        ).render({
            'user' : auth.user(),
        })

class profile(renderer):
    pass

class resume(renderer):
    pass

class index(renderer):
    pass

class login(object):
    def GET(self):
        return auth.login(web.ctx.env.get('HTTP_REFERER'))


class logout(object):
    def GET(self):
        return auth.logout('/')


app = web.application(urls, globals()).wsgifunc()
