#!/usr/bin/env python
import web
import auth
from controller import Controller
from models import Profile, SatSubjectScore, SatScore
from google.appengine.ext import db

class ListController(Controller):

    def __init__(self):
        self.key = str(auth.user().user_id())

    def GET(self):
        if auth.is_admin():
          results = dict()
          for profile in db.GqlQuery("SELECT * FROM Profile ORDER BY uid"):
              results[profile.uid] = profile
          for l in db.GqlQuery("SELECT * FROM LastOnline ORDER BY uid"):
              if l.uid in results:
                  results[l.uid].last_online = l.last_online
          return super(self.__class__, self).GET({'students' : results})
        else:
          return "Access Denied!"

