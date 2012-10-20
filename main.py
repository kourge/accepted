#!/usr/bin/env python
import web, os, jinja2
from google.appengine.api import users
import auth

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

urls = (
    r'/login', 'login',
    r'/logout', 'logout',
    r'/', 'index',
)

class index(object):
    def GET(self):
        user = users.get_current_user()
        if not user:
            name = "Guest"
        else:
            name = user.nickname()
        template_values = {
            'name' : name,
        }      
        template = jinja_environment.get_template('templates/index.html')
        return template.render(template_values)


class login(object):
    def GET(self):
        return auth.login(web.ctx.env.get('HTTP_REFERER'))


class logout(object):
    def GET(self):
        return auth.logout(web.ctx.env.get('HTTP_REFERER'))


app = web.application(urls, globals()).wsgifunc()
