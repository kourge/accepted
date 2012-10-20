#!/usr/bin/env python
import web, os, jinja2
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

urls = (
    r'/.*', 'Hello',
)

class Hello(object):
    def GET(self):
        #return render_template('hello.html', name='world',)
        template_values = {
            'name' : 'Test Name',
        }      
        template = jinja_environment.get_template('templates/hello.html')
        return template.render(template_values)

app = web.application(urls, globals()).wsgifunc()
