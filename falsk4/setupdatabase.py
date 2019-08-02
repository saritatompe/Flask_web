from main import db,Student

db.create_all()

sarita = Student('Sarita',100)
vijaya = Student('Vijaya',105)

print(vijaya.id)
print(sarita.id)

db.session.add_all([sarita,vijaya])

db.session.commit()

print(sarita.id)
print(vijaya.id)
