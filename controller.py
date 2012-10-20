#!/usr/bin/env python
import web
import os
import jinja2

import auth

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Controller(object):
    require_logged_in = False

    def __init__(self):
        if self.require_logged_in and not auth.is_logged_in():
            raise web.notfound()

    def GET(self, variables={}):
        name = self.__class__.__name__.replace('Controller', '').lower()
        defaults = {
            'user' : auth.user(), 'admin' : auth.is_admin()
        }
        defaults.update(variables)

        return jinja_environment.get_template(
            'templates/%s.html' % (name,)
        ).render(defaults)
