#!/usr/bin/env python
import web
from google.appengine.api import users


def user():
    return users.get_current_user()

def is_logged_in():
    return bool(user())

def login(redirect_path):
    if not is_logged_in():
        raise web.redirect(users.create_login_url(redirect_path))

def logout(redirect_path):
    if is_logged_in():
        raise web.redirect(users.create_logout_url(redirect_path))


