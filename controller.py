#!/usr/bin/env python
import web
import os
import jinja2

import auth

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Controller(object):
    def GET(self, variables={}):
        return jinja_environment.get_template(
            'templates/%s.html' % (self.__class__.__name__,)
        ).render(dict({'user': auth.user()}, **variables))
