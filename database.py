
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os.path

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///time-clock3.db'
db = SQLAlchemy(app)

class Project_Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(200), unique=False, nullable=False)       #Project ID
    content = db.Column(db.String(200), unique=False, nullable=False)       #what have I been working on?
    date_start = db.Column(db.String(20), unique=False, nullable=False)     #when did I start my work?
    date_end = db.Column(db.String(20), unique=False, nullable=False)       #when did I finish my work?
    date = db.Column(db.String(20), unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)              #how long did it take?

    def __repr__(self):
        return '<Task %r>' % self.id

class Time_Clock(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.Date, unique=False, nullable=False)
    working_type = db.Column(db.Integer, unique=False, nullable=False)
    
    time_diff = db.Column(db.Float, unique=False, nullable=False)
    overtime = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id

class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200), unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=True)

    def __repr__(self):
        return '<id %r>' % self.id

class Working_Type(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(200), unique=False, nullable=False)
    time = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return '<id %r>' % self.id

if __name__ == "__main__":
    if os.path.isfile('time-clock3.db'):
        print ("File exist")
    else:
        print ("File not exist")
        db.create_all()

        working_type = Working_Type(name = 'Office Day', time=28080)
        projects = Projects(name = 'Testprojekt', time = 60, description ='Das ist ein Test.')
        
        db.session.add(working_type)
        db.session.add(projects)
        db.session.commit()
