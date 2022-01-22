import pymongo
from pymongo import MongoClient
if __name__ == "__main__":
    url = "mongodb+srv://admin:admin@cluster0.ayo4d.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(url)
    db = client.students

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
db.students.find()

db.students.insert({
    "student_id": 1010
    "first_name": "John"
    "last_name": "Doe"
})

print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
db.students.find({
    "student_id": 1010
})

db.student.remove({
    "student_id": 1010
})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
db.students.find()
