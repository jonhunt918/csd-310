MongoDB: find()
docs = db.collection_name.find({})

for doc in docs:
    print(doc)

students.find({})

MongoDB: find_one()
doc = db.collection_name.find_one({"student_id": "1007"})

MongoDB: find_one()
doc = db.collection_name.find_one({"student_id": "1008"})

MongoDB: find_one()
doc = db.collection_name.find_one({"student_id": "1009"})

print(doc["student_id"])