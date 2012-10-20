#!/usr/bin/env python
import web
from controller import Controller

class NotFoundController(Controller):
    def __call__(self):
        return web.notfound(self.GET({'path' : web.ctx.path}))

