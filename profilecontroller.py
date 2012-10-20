#!/usr/bin/env python
import web
from controller import Controller

class ProfileController(Controller):
    def POST(self):
        params = web.input()
        p = Profile.get_or_insert(str(auth.user().user_id()))

        p.firstname = params['firstname']
        p.lastname = params['lastname']
        p.age = params['age']
        p.school = params['school']

        try:
            p.put()
        except TransactionFailedError:
            # Ideally handle the error
            pass

        raise web.redirect(web.ctx.env.get('HTTP_REFERER'))

