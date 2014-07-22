#-*-coding:utf-8-*-
import web
from web.contrib.template import  render_jinja
from os.path import abspath, dirname, join
from jinja2 import Environment, FileSystemLoader


def render_home(template_name, **context):
    extensions = context.pop('extensions', [])
    globals = context.pop('globals', {})
    app = context.pop('app', '')

    jinja_env = Environment(
        loader=FileSystemLoader(join(dirname(__file__), 'templates')),
        extensions=extensions,
    )
    jinja_env.globals.update(globals)

    tpl = app+template_name+'.html'
    #jinja_env.update_template_context(context)
    return jinja_env.get_template(tpl).render(context)