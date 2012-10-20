#!/usr/bin/env python
import web
from google.appengine.ext import db
from google.appengine.api import users

class Profile(db.Model):
    """Models a profile."""
    user = db.UserProperty()
    age = db.IntegerProperty()
    school = db.StringProperty()


class Score(db.Model):
    pass

