from flask import Flask, g, session
from flask_github import GitHub
from dataclasses import asdict
from flaskapp.models import User
from flaskapp.config import Config

app = Flask(__name__)
#Uploading configuration variables, which in fact are environmental, from config.py
app.config.from_object(Config)

github = GitHub(app)

from flaskapp import routes

#setting up our context user
@github.access_token_getter
def token_getter():
    return g.user.oauth_token

@app.before_request
def before_request():
    g.user = User(**session.get('user', {}))

@app.after_request
def after_request(response):
    session['user'] = asdict(g.user)
    return response
