#!/usr/bin/env python
import web
import auth
from controller import Controller
from models import Profile, SatSubjectScore, SatScore

class ProfileController(Controller):

    def __init__(self):
        self.key = str(auth.user().user_id())

    def GET(self):
        p = Profile.get_by_key_name(self.key) or {}
        s = SatScore.get_by_key_name(self.key) or {}
        return super(self.__class__, self).GET({
            'profile' : p,
            'sat' : s,
            'groups' : SatSubjectScore._subject_categories,
            'subjects' : SatSubjectScore._subjects
        })

    def POST(self):
        params = web.input()
        self.process_profile(params)
        self.process_sat(params)

        raise web.redirect(web.ctx.env.get('HTTP_REFERER'))

    def process_profile(self, params):
        attrs = {k : params[k] for k in ['firstname', 'lastname', 'age', 'school']}
        attrs['age'] = int(attrs['age'])
        attrs['uid'] = self.key

        p = Profile.get_by_key_name(self.key)
        if not p:
            p = Profile(key_name=self.key, **attrs)
        else:
            for k, v in attrs.iteritems():
                setattr(p, k, v)

        try:
            p.put()
        except TransactionFailedError:
            # Ideally handle the error
            pass

    def process_sat(self, params):
        attrs = {k : int(params[k]) for k in ['writing', 'reading', 'math']}
        attrs['uid'] = self.key

        s = SatScore.get_by_key_name(self.key)
        if not s:
            s = SatScore(key_name=self.key, **attrs)
        else:
            for k, v in attrs.iteritems():
                setattr(s, k, v)

        try:
            s.put()
        except TransactionFailedError:
            # Ideally handle the error
            pass
