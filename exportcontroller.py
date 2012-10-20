#!/usr/bin/env python
import web
import json
import auth
from controller import Controller
from models import Token, Profile, SatScore, SatSubjectScore
from google.appengine.ext import db

class ExportController(Controller):
    def GET(self, token):
        web.header('Content-Type', 'application/json', unique=True)
        return self.dump(auth.user().user_id())

    def dump(self, uid):
        key = str(uid)
        export = {}
        for model in [Profile, SatScore, SatSubjectScore]:
            e = model.get_by_key_name(key)
            if e:
                export.update(db.to_dict(e))

        return json.dumps(export)

