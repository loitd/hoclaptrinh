from flask import render_template, request, redirect, url_for, session, Blueprint
from werkzeug import generate_password_hash, check_password_hash
from views import curs

registerblp = Blueprint('registerblp', __name__)

# @app.route('/register', methods =['GET'])
@registerblp.route('/register', methods =['GET'])
def getRegister():
    if 'email' in session:
        return redirect(url_for('indexblp.index'))
    else:
        return render_template('register.html')

@registerblp.route('/register', methods=['POST'])
def postRegister():
    try:
        errors = []
        _name = request.form.get('inputName', None)
        _email = request.form.get('inputEmail', None)
        _password = request.form.get('inputPassword', None)
        _hashedpassword = generate_password_hash(_password)
        sql0 = "select count(*) from tbl_users where email = '{0}'".format(_email)
        curs.execute(sql0)
        rows = curs.fetchone()
        if rows and rows[0] > 0:
            errors.append("Email already exists!")
            return render_template('register.html', errors=errors)
        elif _name and _email and _password:
            sql1 = "insert into tbl_users(fullname, email, password) values ('{0}', '{1}', '{2}')".format(_name, _email, _hashedpassword)
            curs.execute(sql1)
            conn.commit()
            return redirect(url_for('loginblp.getLogin'))
    except Exception as e:
        raise(e)