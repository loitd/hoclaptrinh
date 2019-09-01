from flask import Flask, render_template, request, Response, json, session, redirect, url_for, abort, escape, flash
from flaskext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import atexit

app = Flask(__name__)
# secret key for session
app.secret_key = "34567890-cvnbm,./tyijlk;67890vbnm,;ltyuilk.,"
# some securities fixes
app.config.update(
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
)
mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'test'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
curs = conn.cursor()
print("App & Database init done!")

@app.route('/', methods = ['GET'])
def index():
    if 'email' in session:
        _sessionemail = session['email']
        return render_template('index.html')
    else:
        return redirect(url_for('getLogin'))

@app.route('/login', methods=['GET'])
def getLogin():
    if 'email' in session:
        return redirect(url_for('index'))
    else:
        return render_template('login.html')

@app.route('/login', methods=['POST'])
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
            return redirect(url_for('index'))
        else:
            errors.append("Username and password combination not found.")
            return render_template('login.html', errors=errors)
        print("Got: {0}, {1}".format(_email, _password))
    except Exception as e:
        raise(e)
        pass

@app.route('/reg', methods = ['GET'])
def getRegister():
    if 'email' in session:
        return redirect(url_for('index'))
    else:
        return render_template('signup.html')

@app.route('/reg', methods = ['POST'])
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
                return redirect(url_for('getLogin'))
            else:
                errors.append("Email already exists.")
                print(errors)
                return render_template('signup.html', errors=errors)
    except Exception as e:
        raise(e)
        print(e)


@app.route('/logout', methods = ['GET'])
def getLogout():
    session.pop('email', None)
    return redirect(url_for('index'))

def beforeexit(bywho):
    print("Pre-Exit procedures by {0}".format(bywho))
    curs.close()
    conn.close()
# Register atexit procedures
atexit.register(beforeexit, bywho="loitd")

if __name__ == "__main__":
    # debug = True to forece flask reload when code changed
    app.run(debug=True)
    