#!/usr/bin/env python
import web
import auth
from controller import Controller
from models import Profile, SatSubjectScore, SatScore, Activity

class ProfileController(Controller):
    require_logged_in = True

    def __init__(self):
        super(self.__class__, self).__init__()
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
        self.process_sat2(params)
        self.process_extracurriculars(params)

        raise web.redirect(web.ctx.env.get('HTTP_REFERER'))

    def process_profile(self, params):
        attrs = {k : params[k] for k in ['firstname', 'lastname', 'age', 'school']}
        attrs['age'] = int(attrs['age'])
        attrs['uid'] = self.key
        attrs['email'] = auth.user().email();

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

    def process_sat2(self, params):
        attrs = {k : params[k] for k in ['sat_subject', 'sat_subject_score']}
        attrs['subject'] = attrs['sat_subject']
        attrs['score'] = int(attrs['sat_subject_score'])
        attrs['uid'] = self.key

        s = SatSubjectScore.get_by_key_name(self.key)

        if not s:
            s = SatSubjectScore(key_name=self.key, **attrs)
        else:
            for k, v in attrs.iteritems():
                setattr(s, k, v)
        try:
            s.put()
        except TransactionFailedError:
            # Ideally handle the error
            pass

    def process_extracurriculars(self, params):
        attrs = {k : params[k] for k in ['extracurricular', 'extracurricular_start', 'extracurricular_end']}
        attrs['name'] = attrs['extracurricular']
        attrs['uid'] = self.key
        attrs['start_year'] = int(attrs['extracurricular_start'])
        attrs['end_year'] = int(attrs['extracurricular_end'])
        attrs['type'] = 'extracurriculars'

        s = Activity.get_by_key_name(self.key)

        if not s:
            s = Activity(key_name=self.key, **attrs)
        else:
            for k, v in attrs.iteritems():
                setattr(s, k, v)
        try:
            s.put()
        except TransactionFailedError:
            # Ideally handle the error
            pass

