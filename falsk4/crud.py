from main import db,Student

new_student = Student('Gaurav',95)
db.session.add(new_student)
db.session.commit()

all_students = Student.query.all()
print(all_students)

first_student =Student.query.get(1)
print(first_student.name)

student_pass = Student.query.filter(Student.grade>=85)
print(student_pass.all())

first_student = Student.query.get(1)
first_student.grade = 104
db.session.add(first_student)
db.session.commit()

second_student = Student.query.get(3)
db.session.delete(second_student)
db.session.commit()

all_students = Student.query.all()
print(all_students)
