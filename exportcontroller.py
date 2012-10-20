#!/usr/bin/env python
import web
import json
import auth
from controller import Controller
from models import Token, Profile, SatScore, SatSubjectScore
from google.appengine.ext import db

class ExportController(Controller):
    def GET(self, token):
        t = None
        try:
            t = Token.get_by_id(int(token))
        except:
            pass

        if t is None:
            raise web.notfound()

        uid = t.uid
        t.delete()
        web.header('Content-Type', 'application/json', unique=True)
        return self.dump(uid)

    def dump(self, uid):
        key = str(uid)
        export = {}

        for model in [Profile, SatScore]:
            e = model.get_by_key_name(key)
            if e:
                export.update(db.to_dict(e))

        for subject in SatSubjectScore.filter('uid =', uid):
            pass

        return json.dumps(export)

