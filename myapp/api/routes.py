from flask import Blueprint
# api = nombre del modulo
api = Blueprint('api',__name__,url_prefix='/api')

@api.route("/getdata")
def getdata():
    return {'key':'value'}


    # py -m venv env
    # pip install Flask
    # pip install WTForms
    # pip install Flask-SQLAlchemy
    # pip install PyMySQL