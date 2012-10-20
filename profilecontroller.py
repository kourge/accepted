#!/usr/bin/env python
import web
import auth
from controller import Controller
from models import Profile

class ProfileController(Controller):

    def __init__(self):
        self.key = str(auth.user().user_id())

    def GET(self):
        p = Profile.get_by_key_name(self.key) or {}
        return super(self.__class__, self).GET({'profile': p})

    def POST(self):
        params = web.input()
        attrs = {k : params[k] for k in ['firstname', 'lastname', 'age', 'school']}
        attrs['age'] = int(attrs['age'])
        attrs['uid'] = self.key

        p = Profile.get_by_key_name(self.key)
        if not p:
            p = Profile(key_name=self.key, **attrs)
        else:
            for k, v in attrs.items():
                setattr(p, k, v)

        try:
            p.put()
        except TransactionFailedError:
            # Ideally handle the error
            pass

        raise web.redirect(web.ctx.env.get('HTTP_REFERER'))

