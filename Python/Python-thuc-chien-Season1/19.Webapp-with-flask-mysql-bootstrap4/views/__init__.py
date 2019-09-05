from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__, static_folder = '../static', template_folder="../templates")
app.config['MYSQL_DATABASE_USER'] = 'test'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'test'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
# MySQL configurations
mysql.init_app(app)
conn = mysql.connect()
curs = conn.cursor()
print("App & Database init done!")


from views.index import index_blp
from views.login import login_blp
from views.register import register_blp

app.register_blueprint(index_blp)
app.register_blueprint(login_blp)
app.register_blueprint(register_blp)