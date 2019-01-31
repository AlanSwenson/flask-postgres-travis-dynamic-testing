from project import db


class Model1(db.Model):
    __tablename__ = "model1"
    id = db.Column(db.Integer, primary_key=True)
    cool_field = db.Column(db.String(10))
    cooler_field = db.Column(db.String)

    def save(self):
        db.session.add(self)
