from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Use your connection string here
db = client['testdb']  # Database
collection = db['testcollection']  # Collection

# CRUD Operations

# 1. Create (Insert Documents)
doc1 = {"name": "Alice", "age": 25, "hobbies": ["reading", "traveling"]}
doc2 = {"name": "Bob", "age": 30, "hobbies": ["gaming", "coding"]}
doc3 = {"name": "Charlie", "age": 35, "hobbies": ["swimming", "reading"]}
collection.insert_many([doc1, doc2, doc3])
print("Documents inserted.")

# 2. Read (Find Documents)
print("\nRead All Documents:")
for doc in collection.find():
    print(doc)

# 3. Update (Modify Documents)
collection.update_one({"name": "Alice"}, {"$set": {"age": 26}})
collection.update_one({"name": "Bob"}, {"$push": {"hobbies": "hiking"}})  # Add to array
print("\nUpdated Documents:")
for doc in collection.find():
    print(doc)

# 4. Delete (Remove Documents)
collection.delete_one({"name": "Charlie"})
print("\nDocuments After Deletion:")
for doc in collection.find():
    print(doc)

# Working with Arrays
# Query documents containing a specific array value
print("\nDocuments with 'reading' as a hobby:")
for doc in collection.find({"hobbies": "reading"}):
    print(doc)

# Close the connection
client.close()



#output
Documents inserted.

Read All Documents:
{'_id': ObjectId('...'), 'name': 'Alice', 'age': 25, 'hobbies': ['reading', 'traveling']}
{'_id': ObjectId('...'), 'name': 'Bob', 'age': 30, 'hobbies': ['gaming', 'coding']}
{'_id': ObjectId('...'), 'name': 'Charlie', 'age': 35, 'hobbies': ['swimming', 'reading']}

Updated Documents:
{'_id': ObjectId('...'), 'name': 'Alice', 'age': 26, 'hobbies': ['reading', 'traveling']}
{'_id': ObjectId('...'), 'name': 'Bob', 'age': 30, 'hobbies': ['gaming', 'coding', 'hiking']}

Documents After Deletion:
{'_id': ObjectId('...'), 'name': 'Alice', 'age': 26, 'hobbies': ['reading', 'traveling']}
{'_id': ObjectId('...'), 'name': 'Bob', 'age': 30, 'hobbies': ['gaming', 'coding', 'hiking']}

Documents with 'reading' as a hobby:
{'_id': ObjectId('...'), 'name': 'Alice', 'age': 26, 'hobbies': ['reading', 'traveling']}




db.testcollection.insertMany([
  { name: "Alice", age: 25, hobbies: ["reading", "traveling"] },
  { name: "Bob", age: 30, hobbies: ["gaming", "coding"] },
  { name: "Charlie", age: 35, hobbies: ["swimming", "reading"] }
])
db.testcollection.findOne({ name: "Alice" })
op:
{
  "_id": ObjectId("..."),
  "name": "Alice",
  "age": 25,
  "hobbies": ["reading", "traveling"]
}
db.testcollection.updateOne({ name: "Alice" }, { $set: { age: 26 } })
db.testcollection.updateOne({ name: "Bob" }, { $push: { hobbies: "hiking" } })
db.testcollection.deleteOne({ name: "Charlie" })




#count sort skip limit aggregate
// Count all documents in the collection
db.testcollection.countDocuments()

// Count documents where age > 25
db.testcollection.countDocuments({ age: { $gt: 25 } })
// Sort by age in ascending order
db.testcollection.find().sort({ age: 1 })

// Sort by age in descending order
db.testcollection.find().sort({ age: -1 })
// Return only 2 documents
db.testcollection.find().limit(2)
// Skip the first 2 documents and return the rest
db.testcollection.find().skip(2)
// Skip the first document, sort by age in descending order, and limit to 2 results
db.testcollection.find().sort({ age: -1 }).skip(1).limit(2)
db.testcollection.aggregate([
  { $group: { _id: "$age", count: { $sum: 1 } } }
])
db.testcollection.aggregate([
  { $match: { age: { $gt: 25 } } },                // Filter
  { $project: { name: 1, age: 1, _id: 0 } },       // Select fields
  { $sort: { age: 1 } }                            // Sort
])
db.testcollection.aggregate([
  { $group: { _id: null, averageAge: { $avg: "$age" } } }
])

