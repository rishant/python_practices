import pymongo

connect_string =  "mongodb://localhost:27017"

client = pymongo.MongoClient(connect_string)
db = client.get_database('etl_course')
course2_collection = db.get_collection('course2')

for x in course2_collection.find():
  print(x)

print('\n\n')

mydb = client["etl_course"]
mycol = mydb["course"]

for x in mycol.find():
  print(x)

for x in mycol.find({},{ "course_name": 1, "author_name": 1, "_id": 0 }):
  print(x)
#
# with open("data.json", "a") as f:
#   for x in mycol.find():
#     f.write(json.dumps(x) + ',\n')
