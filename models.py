#!/usr/bin/env python
import web
from google.appengine.ext import db


class Profile(db.Model):
    """Models a profile."""
    # We should explicitly store the user ID, since the User object does not update
    # accordingly when the user changes email address.
    uid = db.IntegerProperty(required=True, indexed=True)

    age = db.IntegerProperty(required=True)
    school = db.StringProperty(required=True)


class Activity(db.Model):
    """An activity such as sports or extracurriculars."""
    type = db.StringProperty(
        required=True, choices=set(['sports', 'extracurriculars'])
    )
    name = db.StringProperty(required=True)
    start_year = db.IntegerProperty(required=True)
    end_year = db.IntegerProperty()


def validate_sat_score(value):
    if not (value <= 800 and value >= 200):
        raise db.BadValueError()


class SatScore(db.Model):
    writing = db.IntegerProperty(required=True, validator=validate_sat_score)
    reading = db.IntegerProperty(required=True, validator=validate_sat_score)
    math = db.IntegerProperty(required=True, validator=validate_sat_score)


