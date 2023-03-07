from flask import Flask
from flask import Blueprint
from .api.routes import api
from site.routes import site

api = Blueprint('api',__name__,url_prefix='/api')


def create_app():
    app=Flask(__name__)
    app.register_blueprint(api)
    app.register_blueprint(site)
    return app
    