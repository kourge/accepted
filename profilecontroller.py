#!/usr/bin/env python
import web
from controller import Controller

class ProfileController(Controller):
    def POST(self):
        # p = Profile.get_or_insert(str(auth.user().user_id()))
        return repr(web.input().keys())

