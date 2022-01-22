import pymongo
from pymongo import MongoClient
if __name__ == "__main__":
    url = "mongodb+srv://admin:admin@cluster0.ayo4d.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(url)
    db = client.students

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- ")
db.students.find()

db.students.update({
    "student_id": 1007
},
{
    $set:
    {"last_name": "Oakenshield II"}
})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 -- ")
db.students.find({
    "student_id": 1007
})

    
