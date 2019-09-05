from views import curs
from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint
from werkzeug import generate_password_hash, check_password_hash

login_blp = Blueprint('login_blp', __name__)

# @app.route('/login', methods=['GET'])
@login_blp.route('/login', methods=['GET'])
def getLogin():
    if 'email' in session:
        return redirect(url_for('index_blp.index'))
    else:
        return render_template('login.html')

# @app.route('/login', methods=['POST'])
@login_blp.route('/login', methods=['POST'])
def postLogin():
    try:
        errors = []
        _email = request.form.get('inputEmail', None)
        _password = request.form.get('inputPassword', None)
        sql = "SELECT password FROM TBL_USERS WHERE EMAIL = '{0}'".format(_email)
        curs.execute(sql)
        rows = curs.fetchone()
        hashedpassword = rows[0]
        # print(rows)
        if rows and check_password_hash(hashedpassword, _password):
            session['email'] = _email
            print("session set")
            return redirect(url_for('index_blp.index'))
        else:
            errors.append("Username and password combination not found.")
            return render_template('login.html', errors=errors)
        print("Got: {0}, {1}".format(_email, _password))
    except Exception as e:
        raise(e)
        pass

# @app.route('/logout', methods = ['GET'])
@login_blp.route('/logout', methods = ['GET'])
def getLogout():
    session.pop('email', None)
    return redirect(url_for('index_blp.index'))