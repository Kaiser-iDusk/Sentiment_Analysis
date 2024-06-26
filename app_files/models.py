from app_files import db

class URL_Yelp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    polarity = db.Column(db.Float, nullable=False)