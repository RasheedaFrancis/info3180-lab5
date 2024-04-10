from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config



app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from app import views
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
migrate = Migrate(app, db) 
csfr = CSRFProtect(app)
