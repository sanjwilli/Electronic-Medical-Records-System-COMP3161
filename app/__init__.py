from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
db = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hacker303'
app.config['MYSQL_DATABASE_DB'] = 'hospital'
db.init_app(app)

#db = MySQL(app)

app.config.from_object(__name__)
from app import views