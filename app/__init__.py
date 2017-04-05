from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql9167295'
app.config['MYSQL_PASSWORD'] = '5hF7CmPhPD'
app.config['MYSQL_DB'] = 'sql9167295'

db = MySQL(app)

app.config.from_object(__name__)
from app import views