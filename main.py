#!/usr/bin/env python
import web, os, jinja2
from google.appengine.api import users
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

urls = (
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

app = web.application(urls, globals()).wsgifunc()
