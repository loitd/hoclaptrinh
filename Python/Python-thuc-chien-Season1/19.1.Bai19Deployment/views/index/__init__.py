from flask import render_template, request, redirect, url_for, session, Blueprint
from views import curs

indexblp = Blueprint('indexblp', __name__)

# @app.route('/', methods=['GET'])
@indexblp.route('/', methods=['GET'])
def index():
    if 'email' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('loginblp.getLogin'))