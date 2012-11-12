#!/usr/bin/env python
import web
import auth
import itertools
from controller import Controller
from models import Profile, SatSubjectScore, SatScore, Activity
from google.appengine.ext.db import TransactionFailedError

class ProfileController(Controller):
    require_logged_in = True

    def __init__(self):
        super(self.__class__, self).__init__()
        self.key = str(auth.user().user_id())

    def GET(self):
        p = Profile.get_by_key_name(self.key) or {}
        s = SatScore.get_by_key_name(self.key) or {}
        sat2s = SatSubjectScore.all().filter('uid =', self.key)
        return super(self.__class__, self).GET({
            'profile' : p,
            'sat' : s,
            'sat2s' : sat2s,
            'groups' : SatSubjectScore._subject_categories,
            'subjects' : SatSubjectScore._subjects
        })

    def POST(self):
        self.process_profile()
        self.process_sat()
        self.process_sat2()
        for activity in Activity._activities:
            self.process_activities(activity)

        raise web.redirect(web.ctx.env.get('HTTP_REFERER'))

    def process_profile(self):
        params = web.input()
        keys = ['firstname', 'lastname', 'age', 'school']

        attrs = { k : params[k] for k in keys }
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

    def process_sat(self):
        params = web.input()
        attrs = { k : int(params[k]) for k in ['writing', 'reading', 'math'] }
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

    def process_sat2(self):
        params = web.input(sat_subject=[], sat_subject_score=[])
        subjects = params.sat_subject
        scores = params.sat_subject_score
        score_pairs = dict(itertools.izip(subjects, scores))

        for known in SatSubjectScore.all().filter('uid =', self.key):
            # Update existing scores
            if known.subject in subjects:
                new_score = score_pairs[known.subject]
                known.score = int(new_score)
                try:
                    known.put()
                except TransactionFailedError:
                    # Ideally handle the error
                    pass

                subjects.remove(known.subject)
                del score_pairs[known.subject]

            # Delete a removed score
            else:
                known.delete()

        # Insert new scores
        for subject, score in score_pairs.iteritems():
            subject_score = SatSubjectScore(
                uid=self.key, subject=subject, score=score
            )
            try:
                subject_score.put()
            except TransactionFailedError:
                # Ideally handle the error
                pass

    def process_activities(self, category):
        pass

