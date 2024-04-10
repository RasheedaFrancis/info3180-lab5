# Add any model classes for Flask-SQLAlchemy here
from . import db


class Movie(db.Model):
     __tablename__ = 'movies'
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(255))
     description = db.Column(db.Text)
     poster = db.Column(db.String(255))
     created_at = db.Column(db.DateTime)
    
    
     def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at


     def is_authenticated(self):
        return True

     def is_active(self):
        return True

     def is_anonymous(self):
        return False

     def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

     def __repr__(self):
        return '<User %r>' % (self.username)