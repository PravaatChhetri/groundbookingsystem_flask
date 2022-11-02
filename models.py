import mimetypes
from datetime import datetime
from db import db


class userInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(10), nullable=False)
    dy = db.Column(db.String(10), nullable=True)
    password=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return '<User %r>' % self.dy

    def __init__(self, email, role, dy,password):
        self.email = email
        self.role = role
        self.dy = dy
        self.password=password

class Grounds(db.Model):
    gId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    groundName = db.Column(db.String(100), unique=True, nullable=False)
    NoOfCourt = db.Column(db.Integer, nullable=False)
    bookTime = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Ground %r>' % self.groundName

    def __init__(self, groundName, NoOfCourt, bookTime):
        self.groundName = groundName
        self.NoOfCourt = NoOfCourt
        self.bookTime = bookTime

class Bookings(db.Model):
    bId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ground = db.Column(db.String(100), nullable=False)
    team_1 = db.Column(db.String(10), nullable=False)
    team_2 = db.Column(db.String(10), nullable=False)
    courtName = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(100), nullable=False)
#    bookedBy=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return '<Book ID %r>' % self.bId

    def __init__(self, ground, team_1, team_2, courtName, date, time):
        self.ground = ground
        self.team_1 = team_1
        self.team_2 = team_2
        self.courtName = courtName
        self.date = date
        self.time = time

class Blogs(db.Model):
    BId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    image = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Blog %r>' % self.title

    def __init__(self, title, content, author, image, mimetype):
        self.title = title
        self.content = content
        self.author = author
        self.image = image
        self.mimetype = mimetype
    
