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
          q = db.GqlQuery("SELECT * FROM Profile")
          return super(self.__class__, self).GET({'students' : q})
        else:
          return "Access Denied!"

