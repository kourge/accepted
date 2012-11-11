#!/usr/bin/env python
import web
from google.appengine.ext import db


class Activity(db.Model):
    uid = db.StringProperty(required=True, indexed=True)

    type = db.StringProperty(
        required=True, choices=set(['sports', 'extracurriculars', 'work'])
    )
    name = db.StringProperty(required=True)
    start_year = db.IntegerProperty(required=True)
    end_year = db.IntegerProperty()


def validate_sat_score(value):
    if not (value <= 800 and value >= 200):
        raise db.BadValueError()


class SatScore(db.Model):
    uid = db.StringProperty(required=True, indexed=True)

    writing = db.IntegerProperty(required=True, validator=validate_sat_score)
    reading = db.IntegerProperty(required=True, validator=validate_sat_score)
    math = db.IntegerProperty(required=True, validator=validate_sat_score)

class SatSubjectScore(db.Model):
    uid = db.StringProperty(required=True, indexed=True)

    _subjects = {
        'General': [
            'Literature', 'United States (U.S.) History', 'World History',
            'Mathematics Level 1', 'Mathematics Level 2',
            'Biology E/M (Ecological/Molecular)', 'Chemistry', 'Physics'
        ],

        'Languages: Reading Only': [
            'French (Reading Only)', 'German (Reading Only)',
            'Modern Hebrew (Reading Only)', 'Italian (Reading Only)',
            'Latin (Reading Only)', 'Spanish (Reading Only)'
        ],

        'Languages: Reading and Listening': [
            'Chinese (Reading and Listening)', 'French (Reading and Listening)',
            'German (Reading and Listening)', 'Japanese (Reading and Listening)',
            'Korean (Reading and Listening)', 'Spanish (Reading and Listening)'
        ]
    }

    _subject_categories = [
        'General', 'Languages: Reading Only', 'Languages: Reading and Listening'
    ]

    subject = db.StringProperty(
        required=True
    )
    score = db.IntegerProperty(required=True, validator=validate_sat_score)


class Profile(db.Model):
    # We should explicitly store the user ID, since the User object does not update
    # accordingly when the user changes email address.
    uid = db.StringProperty(required=True, indexed=True)

    firstname = db.StringProperty(required=True)
    lastname = db.StringProperty(required=True)

    age = db.IntegerProperty(required=True)
    school = db.StringProperty(required=True)

    email = db.EmailProperty(required=True)


class LastOnline(db.Model):
    uid = db.StringProperty(required=True, indexed=True)
    last_online = db.DateTimeProperty(required=True, auto_now=True)


