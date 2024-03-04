import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager,UserMixin
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '0273e94a47bb8f15372775f2404c9f38'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@localhost/site"
db = SQLAlchemy(app)
login_manager = LoginManager(app)
migrate = Migrate(app,db)


from File_editor import routes