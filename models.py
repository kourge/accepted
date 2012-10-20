#!/usr/bin/env python
import web
from google.appengine.ext import db


class Profile(db.Model):
    """Models a profile."""
    # We should explicitly store the user ID, since the User object does not update
    # accordingly when the user changes email address.
    uid = db.IntegerProperty(required=True, indexed=True)

    firstname = db.StringProperty(required=True)
    lastname = db.StringProperty(required=True)

    age = db.IntegerProperty(required=True)
    school = db.StringProperty(required=True)

    activities = db.ListProperty(Activity)
    sat_score = db.ReferenceProperty(SatScore)
    sat_subject_scores = db.ListProperty(SatSubjectScore)


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

class SatSubjectScore(db.Model):
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
        required=True, choices=set([x for l in _subjects.values() for x in l])
    )
    score = db.IntegerProperty(required=True, validator=validate_sat_score)


