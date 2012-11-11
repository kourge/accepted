#!/usr/bin/env python
import web
import auth
import json
import base64
from google.appengine.ext import db
from controller import Controller
from models import Profile, SatScore

class ResumeController(Controller):
    require_logged_in = True

    SCRIPT_ID = 'AKfycbxzldDtnjeVMTEHjK5i4aYnFmNmryHf5qbVVqXal5uD6Dc48Hyb'
    SCRIPT_URL = 'https://script.google.com/macros/s/%s/exec' % (SCRIPT_ID,)

    def GET(self):
        return super(self.__class__, self).GET({
            'script_url' : self.SCRIPT_URL,
            'data' : base64.b64encode(self.dump())
        })

    def dump(self):
        key = str(auth.user().user_id())
        export = {}

        for model in [Profile, SatScore]:
            e = model.get_by_key_name(key)
            if e:
                export.update(db.to_dict(e))

        #for subject in SatSubjectScore.filter('uid =', uid):
        #    pass

        return json.dumps(export)


