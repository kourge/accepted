#!/usr/bin/env python
import web
from controller import Controller

class ResumeController(Controller):
    require_logged_in = True

    def __init__(self):
        super(self.__class__, self).__init__()

