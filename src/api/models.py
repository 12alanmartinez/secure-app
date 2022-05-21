from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    eyeColor = db.Column(db.String(150), unique=False, nullable=True)
    hairColor = db.Column(db.String(150), unique=False, nullable=True)
    skinColor = db.Column(db.String(150), unique=False, nullable=True)
    height = db.Column(db.Sting(150), unique=False, nullable=True)
    mass = db.Column(db.String(150), unique=False, nullable=True)
    birthYear = db.Column(db.Sting(150) unique=False, nullable=True)

# ---------------------------------------------------------------------


class planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
