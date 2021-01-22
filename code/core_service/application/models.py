from application import db

class Buy(db.Model):
    __tablename__  = 'buy'
    id = db.Column(db.Integer, primarykey=true, autoincrement=true)
    roundstrength= = db.Column(db.String(5),nullable=False)
    weapon = db.Column(db.String(30),nullable=False)
    strat = db.Column(db.String(30),nullable=False)
