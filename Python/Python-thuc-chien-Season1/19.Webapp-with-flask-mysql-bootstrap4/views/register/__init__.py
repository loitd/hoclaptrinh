from views import curs
from flask import render_template, request, Response, json, session, redirect, url_for, abort, escape, flash, Blueprint
from werkzeug import generate_password_hash, check_password_hash

register_blp = Blueprint('register_blp', __name__)

# @app.route('/reg', methods = ['GET'])
@register_blp.route('/reg', methods = ['GET'])
def getRegister():
    if 'email' in session:
        return redirect(url_for('index_blp.index'))
    else:
        return render_template('signup.html')

# @app.route('/reg', methods = ['POST'])
@register_blp.route('/reg', methods = ['POST'])
def postRegister():
    try:
        # print("Begin processing postRegister")
        errors = []
        _name = request.form.get('inputName', None)
        _email = request.form.get('inputEmail', None)
        _password = request.form.get('inputPassword', None)
        _hashpassword = generate_password_hash(_password)
        print("Got: {0}, {1}, {2}, {3}".format(_name, _email, _password, _hashpassword))
        if _name and _email and _password:
            sql0 = "SELECT COUNT(*) FROM tbl_users WHERE EMAIL = '{0}'".format(_email)
            sql1 = "INSERT INTO tbl_users (email, password, fullname, status) VALUES ('{0}', '{1}', '{2}', 0)".format(_email, _hashpassword, _name)
            curs.execute(sql0)
            rows = curs.fetchone()
            if rows[0] == 0:
                curs.execute(sql1)
                conn.commit()
                return redirect(url_for('login_blp.getLogin'))
            else:
                errors.append("Email already exists.")
                print(errors)
                return render_template('signup.html', errors=errors)
    except Exception as e:
        raise(e)
        print(e)