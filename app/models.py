from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text)
    status_code = db.Column(db.Integer)
    suggested_alternative = db.Column(db.Text)
