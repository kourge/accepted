#!/usr/bin/env python
import web
import os
import jinja2

import auth
from models import LastOnline

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
            'user' : auth.user(), 'admin' : auth.is_admin(), 'path' : web.ctx.path
        }
        defaults.update(variables)

        if auth.user():
            lastonline = LastOnline.get_by_key_name(str(auth.user().user_id())) 
            if not lastonline:
                lastonline = LastOnline(key_name=str(auth.user().user_id()), uid=str(auth.user().user_id())) 
            lastonline.put()

        return jinja_environment.get_template(
            'templates/%s.html' % (name,)
        ).render(defaults)
