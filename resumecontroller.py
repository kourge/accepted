#!/usr/bin/env python
import web
import auth
from controller import Controller
from models import Token

class ResumeController(Controller):
    pass


class ResumeGenerationController(Controller):
    SCRIPT_ID = 'AKfycbxzldDtnjeVMTEHjK5i4aYnFmNmryHf5qbVVqXal5uD6Dc48Hyb'
    SCRIPT_URL = 'https://script.google.com/macros/s/%s/exec' % (SCRIPT_ID,)

    def GET(self):
        t = Token(uid=auth.user().user_id())

        try:
            t.put()
        except:
            pass

        token = t.key().id()
        raise web.redirect('%s?token=%s' % (self.SCRIPT_URL, token))


