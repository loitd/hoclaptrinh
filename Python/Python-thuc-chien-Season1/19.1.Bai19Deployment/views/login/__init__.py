from flask import render_template, request, redirect, url_for, session, Blueprint
from werkzeug import generate_password_hash, check_password_hash
from views import curs

loginblp = Blueprint('loginblp', __name__)

# @app.route('/logout', methods=['GET'])
@loginblp.route('/logout', methods=['GET'])
def getLogout():
    session.pop('email')
    return redirect(url_for('loginblp.getLogin'))


@loginblp.route('/login', methods=['GET'])
def getLogin():
    if 'email' in session:
        return redirect(url_for('indexblp.index'))
    else:
        return render_template('login.html')

@loginblp.route('/login', methods=['POST'])
def postLogin():
    try:
        errors = []
        _email = request.form.get('inputEmail', None)
        _password = request.form.get('inputPassword', None)
        sql0 = "select password from tbl_users where email = '{0}'".format(_email)
        curs.execute(sql0)
        rows = curs.fetchone()
        if rows:
            dbPassword = rows[0]
            if check_password_hash(dbPassword, _password):
                session['email'] = _email
                return redirect(url_for('indexblp.index'))
            else:
                errors.append("Email/password combination not found!")
                return render_template('login.html', errors=errors)
    except Exception as e:
        raise(e)