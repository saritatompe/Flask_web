import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Student(db.Model):
    __tablename__ ="students"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    grade=db.Column(db.Integer)

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def __repr__(self):
        return f"Student {self.name} got {self.grade} on midterm exam"


if __name__ == "__main__":
    app.run(debug=True)
