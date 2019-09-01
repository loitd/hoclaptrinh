from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug import generate_password_hash, check_password_hash
from flaskext.mysql import MySQL
app = Flask(__name__)
app.secret_key = 'dsaoijlkfddnklsaddkjsafd'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'test'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'test'

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
curs = conn.cursor()
print("Connect to database successfully.")

@app.route('/', methods=['GET'])
def index():
    if 'email' in session:
        return render_template('index.html')
    else:
        return redirect(url_for('getLogin'))
  
@app.route('/logout', methods=['GET'])
def getLogout():
    session.pop('email')
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
        sql0 = "select password from tbl_users where email = '{0}'".format(_email)
        curs.execute(sql0)
        rows = curs.fetchone()
        if rows:
            dbPassword = rows[0]
            if check_password_hash(dbPassword, _password):
                session['email'] = _email
                return redirect(url_for('index'))
            else:
                errors.append("Email/password combination not found!")
                return render_template('login.html', errors=errors)
    except Exception as e:
        raise(e)

@app.route('/register', methods =['GET'])
def getRegister():
    if 'email' in session:
        return redirect(url_for('index'))
    else:
        return render_template('register.html')

@app.route('/register', methods=['POST'])
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
            return redirect(url_for('getLogin'))
    except Exception as e:
        raise(e)

if __name__ == "__main__":
    app.run(debug=True)
    # pipenv run python main.py
    