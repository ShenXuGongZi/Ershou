#-*- coding: utf-8 -*
#import web
from main import *

urls = (
    '/', 'index',
    "/index/page/(\d+)", "page",
    "/game/page/(\d+)", "game",
    "/shuma/page/(\d+)", "shuma",
    # "/search", "search",
    "/search/(.*)", "SomePage",
)


app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
