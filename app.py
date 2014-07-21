#-*- coding: utf-8 -*
#import web
from setting import *

urls = (
    '/', 'index',
    '/page/(\d+)','NavNum',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
