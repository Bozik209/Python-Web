import pymongo

uri = "mongodb://127.0.0.1:27017" 
client = pymongo.MongoClient("localhost", 27017)  # or client=pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']


# option 1 
students = collection.find({})
students_list=[]

for target_list in students:
    students_list.append(target_list)
    print(target_list)

''' ------------------OUTPUT------------------
# {'_id': ObjectId('5dc4289f42e0ad95935215d8'), 'name': 'bob', 'age': 15.0}
# {'_id': ObjectId('5dc4296842e0ad95935215d9'), 'name': 'alice', 'age': 21.0}
'''

# option 2
student = [students for students in collection.find({})]
print(student)
''' ------------------OUTPUT------------------
[{'_id': ObjectId('5dc4289f42e0ad95935215d8'), 'name': 'bob', 'age': 15.0}, {'_id': ObjectId('5dc4296842e0ad95935215d9'), 'name': 'alice', 'age': 21.0}]
'''

student = [students['name'] for students in collection.find({})]
print(student)
''' ------------------OUTPUT------------------
# ['bob', 'alice']
'''

# if
student = [students['name'] for students in collection.find({}) if students['name'] == "bob"]
print(student)
''' ------------------OUTPUT------------------ 
# ['bob']
'''