#-*- coding: utf-8 -*
#import web
from main import *

urls = (
    '/', 'index',
    "/index/page/(\d+)", "page",
    "/game/page/(\d+)", "game",
    "/smzj/page/(\d+)", "shuma",
    "/weifeng/page/(\d+)", "weifeng",
    # "/search", "search",
    "/search/(.*)", "SomePage",
)


app = web.application(urls, globals())
ershou = app.wsgifunc()

if __name__ == "__main__":
    app.run()
