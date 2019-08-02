#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import os
from flask import Flask
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' \
    + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRAC_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Student(db.Model):
    #title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    __tablename__ ="student"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    grade=db.Column(db.Integer)

    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

    def __repr__(self):
        return "Student {self.name} got {self.grade} on midterm exam"

@app.route('/', methods=["GET", "POST"])
def home():
    students = None
    if request.form:
        try:
            student = Student(name=request.form.get("name"),grade=request.form.get("grade"))
            db.session.add(student)
            db.session.commit()
        except Exception as e:
            print("Failed to add student")
            print(e)
    students = Student.query.all()
    return render_template("home.html", students=students)

@app.route("/update", methods=["POST"])
def update():
    try:
        newgrade = request.form.get("newgrade")
        oldgrade = request.form.get("oldgrade")
        student = Student.query.filter_by(grade=oldgrade).first()
        student.grade = newgrade
        db.session.commit()
    except Exception as e:
        print("Couldn't update student grade")
        print(e)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    student = Student.query.filter_by(name=name).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
