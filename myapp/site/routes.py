from flask import Blueprint
# api = nombre del modulo
site = Blueprint('site',__name__)

@site.route("/")
def index():
    return 'Iñdex '