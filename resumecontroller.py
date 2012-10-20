#!/usr/bin/env python
import web
from controller import Controller

class ResumeController(Controller):
    SCRIPT_ID = 'AKfycbxzldDtnjeVMTEHjK5i4aYnFmNmryHf5qbVVqXal5uD6Dc48Hyb'
    SCRIPT_URL = 'https://script.google.com/macros/s/%s/exec' % (SCRIPT_ID,)

