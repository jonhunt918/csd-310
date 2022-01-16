import pymongo

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.mg0m3.mongodb.net/Pytech?retryWrites=true&w=majority"

client = MongoClient('localhost', 27017)

db = client.pytech

print("\n -- Pytech Collection List --")
print(db.list_collection_names)
input("\nEnd of program, press any key to exit...\n")
