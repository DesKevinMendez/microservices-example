from flask import abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    def json(self):
        if self is not None:
            return {'id': self.id, 'email': self.email}
        else: abort(404, description="User not found")
        # this method we are defining will convert our output to json

    def add_user(_email):
        # creating an instance of our User constructor
        new_user = User(email=_email)
        db.session.add(new_user)  # add new movie to database session
        db.session.commit()  # commit changes to session

    def get_all_users():
        '''function to get all movies in our database'''
        return [User.json(user) for user in User.query.all()]

    def get_user(_id):
        return User.json(User.query.filter_by(id=_id).first())

    def get_user_by_email(email):
        return User.json(User.query.filter_by(email=email).first())

    def update_user(_id, _email):
        user_to_update = User.query.filter_by(id=_id).first()
        if user_to_update is None:
            abort(404, description="User not found")
        user_to_update.email = _email
        db.session.commit()
        return User.json(user_to_update)

    def delete_user(_id):
        User.query.filter_by(id=_id).delete()
        db.session.commit()
