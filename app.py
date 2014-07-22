#-*- coding: utf-8 -*
#import web
from main import *

urls = (
    '/', 'index',
    "/page/(\d+)", "news",
)

class SomePage:
    def POST(self):
        # Do some application logic here, and then:
        raise web.seeother('/someotherpage')

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
