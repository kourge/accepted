#!/usr/bin/env python
import web
import auth
from controller import Controller
from models import Profile, SatSubjectScore, SatScore, LastOnline
from google.appengine.ext import db

class ListController(Controller):

    def __init__(self):
        self.key = str(auth.user().user_id())

    def GET(self, name=None):
        if auth.is_admin():
            found_name = False
            if name:
               q = Profile.all().filter('uid =', name).get()
               if q:
                  found_name = True
                  return self.individual_profile(q)

            if not found_name:
                results = dict()
                for profile in db.GqlQuery("SELECT * FROM Profile"):
                    results[profile.uid] = profile
                for l in db.GqlQuery("SELECT * FROM LastOnline"):
                    if l.uid in results:
                        results[l.uid].last_online = l.last_online
                return super(self.__class__, self).GET({'students' : results})
        else:
          return "Access Denied!"

    def individual_profile(self, p):
        q = LastOnline.all().filter('uid =', p.uid).get()
        return super(self.__class__, self).GET({'student' : p, 'activity' : q})
