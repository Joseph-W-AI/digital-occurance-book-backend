# app.py

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///digital_occurrence_book.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'abc123'
    
    CORS(app)
    
    api = Api(app)
    
    from .models import db
    db.init_app(app)

    from .controllers import Register, Login, IndividualUser, Incidents, AllUsers, IndividualIncident
    api.add_resource(Register, '/register')
    api.add_resource(Login, '/login')
    api.add_resource(AllUsers, '/users')
    api.add_resource(IndividualUser, '/users/<int:user_id>')
    api.add_resource(Incidents, '/incidents')
    api.add_resource(IndividualIncident, '/incidents/<int:incident_id>')

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
