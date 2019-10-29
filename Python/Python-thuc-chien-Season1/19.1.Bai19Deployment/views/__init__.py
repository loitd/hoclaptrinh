from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__, static_folder='../static', template_folder='../templates')
app.secret_key = 'dsaoijlkfddnklsa65789ddkjsafd'

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'test'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'test'

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
curs = conn.cursor()
print("Connect to database successfully.")

from views.index import indexblp
from views.login import loginblp
from views.register import registerblp

app.register_blueprint(indexblp)
app.register_blueprint(loginblp)
app.register_blueprint(registerblp)

