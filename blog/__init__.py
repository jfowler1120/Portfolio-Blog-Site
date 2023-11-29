from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c398a302920e2e38456f11e687473772469ee141095bef46'

app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://c1816886:R0cksteady?@csmysql.cs.cf.ac.uk:3306/c1816886_alpacaSoft'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from blog import routes







