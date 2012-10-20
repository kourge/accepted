#!/usr/bin/env python
import web
import auth
from controller import Controller
from models import Profile

class ProfileController(Controller):
    def GET(self):
        key = str(auth.user().user_id())
        p = Profile.get_by_key_name(key) or {}
        return super(self.__class__, self).GET({'profile': p})

    def POST(self):
        params = web.input()
        key = str(auth.user().user_id())

        attrs = {k : params[k] for k in ['firstname', 'lastname', 'age', 'school']}
        attrs['age'] = int(attrs['age'])
        attrs['uid'] = key

        p = Profile.get_by_key_name(key) or Profile(key_name=key, **attrs)

        try:
            p.put()
        except TransactionFailedError:
            # Ideally handle the error
            pass

        raise web.redirect(web.ctx.env.get('HTTP_REFERER'))

