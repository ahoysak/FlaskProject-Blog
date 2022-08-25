from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'myuniqpasswordforflaskapplication'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://artur:flask@mysql/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)


with app.app_context():

    from routes.article import *
    from routes.routes import *
    from routes.registration import *
    from routes.login import *

    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
