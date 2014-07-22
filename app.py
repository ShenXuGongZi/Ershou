#-*- coding: utf-8 -*
#import web
from main import *

urls = (
    '/', 'index',
    "/index/page/(\d+)", "news",
    "/tag/page/(\d+)", "tag",
)


app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
