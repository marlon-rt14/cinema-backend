from utils.db import db

class Movie(db.Model):
    __tablename__ = 'movies'
    valid_properties = ['id', 'title', 'year', 'rating']
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=True)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def serialize(self) -> dict:
        instance_dict =  vars(self)
        instance_dict.pop('_sa_instance_state', None)
        return instance_dict