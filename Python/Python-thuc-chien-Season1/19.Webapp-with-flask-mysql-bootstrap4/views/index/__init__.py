from views import curs
from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint
from werkzeug import generate_password_hash, check_password_hash

# https://flask.palletsprojects.com/en/1.1.x/blueprints/
index_blp = Blueprint('index_blp', __name__)

# @app.route('/', methods = ['GET'])
@index_blp.route('/', methods = ['GET'])
def index():
    if 'email' in session:
        _sessionemail = session['email']
        return render_template('index.html')
    else:
        return redirect(url_for('login_blp.getLogin'))
