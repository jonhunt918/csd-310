import pymongo
from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client["pytech"]
students = db["pytech"]

print("\n -- INSERT STATEMENTS -- ")

MongoDB: insert_one() 
thorin = {
    "first_name": "Thorin", "last_name":"Oakenshield", "student_id": 1007
}
thorin_student_id = students.insert_one(thorin).inserted_id

print("Inserted student record Thorin Oakenshield into the students collection with document_id", thorin_student_id)

MongoDB: insert_one()
bilbo = {
    "first_name": "Bilbo", "last_name": "Baggins", "student_id": 1008
}
bilbo_student_id = students.insert_one(bilbo).inserted_id

print("Inserted student record Thorin Oakenshield into the students collection with document_id", bilbo_student_id)

MongoDB: insert_one()
frodo = {
    "first_name": "Frodo", "last_name": "Baggins", "student_id": 1009
}
frodo_student_id = students.insert_one(frodo).inserted.id

print("Inserted student record Thorin Oakenshield into the students collection with document_id", frodo_student_id)

print(thorin_student_id, bilbo_student_id, frodo_student_id)

