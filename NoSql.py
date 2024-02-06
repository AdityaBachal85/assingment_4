

''' 
Q1. What is MongoDB? Explain non-relational databases in short. In which scenarios it is preferred to use MongoDB over SQL databases?

MongoDB: MongoDB is a popular open-source NoSQL database that stores data in flexible, JSON-like documents. 
It offers high scalability and performance, making it suitable for applications with rapidly changing data requirements, such as social media, real-time analytics, and content management systems.

Non-relational databases: Non-relational databases, also known as NoSQL databases, are designed to handle large volumes of unstructured or semi-structured data. 
Unlike SQL databases, they don't rely on fixed schemas, allowing for more flexibility and scalability. 

Scenarios for using MongoDB over SQL databases:

Flexible Schema: When the data structure is dynamic and subject to frequent changes.
Scalability: MongoDB's distributed architecture makes it suitable for scaling horizontally across multiple servers.
Big Data and Real-time Analytics: In scenarios where real-time data processing and analysis are crucial.
Document-oriented Storage: For applications that deal with JSON-like data structures or nested arrays/documents.
'''

''' 
Q2. State and Explain the features of MongoDB.

Features of MongoDB:

Document-Oriented: Stores data in flexible JSON-like documents.

Scalable: Supports horizontal scaling by sharding data across multiple servers.

High Performance: Offers high throughput and low latency for read and write operations.

Rich Query Language: Supports a wide range of queries including field, range, and regular expression queries.

Indexes: Allows for efficient querying by creating indexes on fields.

Aggregation Framework: Provides tools for performing data aggregation operations.

Flexible Schema: Supports dynamic schema design, enabling easier data modeling and evolution.

Replication and High Availability: Supports automatic failover and data redundancy through replica sets.
Geospatial Indexes: Enables querying of geospatial data.

Ad Hoc Queries: Allows for ad hoc queries without requiring predefined schemas.

GridFS: A specification for storing large files in MongoDB. 
'''

''' Q3. Write a code to connect MongoDB to Python. Also, create a database and a collection in MongoDB.'''
import pymongo

# Connect to MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create a database
mydb = client["mydatabase"]

# Create a collection
mycol = mydb["customers"]
  

'''
Q4. Using the database and the collection created in question number 3,
write a code to insert one record, and insert many records. 
Use the find() and find_one() methods to print the inserted record
'''

# Insert one record
record = {"name": "John", "address": "Highway 37"}
mycol.insert_one(record)

# Insert many records
records = [
    {"name": "Peter", "address": "Lowstreet 27"},
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"}
]
mycol.insert_many(records)

# Find one record
print(mycol.find_one())

# Find all records
for record in mycol.find():
    print(record)


'''
Q5. Explain how you can use the find() method to query the MongoDB database. Write a simple code to demonstrate this.

The find() method in MongoDB is used to query documents in a collection. 
It returns a cursor object that can be iterated over to retrieve documents.
'''
# Query documents
for document in mycol.find({"name": "John"}):
    print(document)

'''
Q6. Explain the sort() method. Give an example to demonstrate sorting in MongoDB.

The sort() method in MongoDB is used to sort the results of a query based on one or more fields.
'''

# Sort documents by name in ascending order
for document in mycol.find().sort("name"):
    print(document)

# Sort documents by name in descending order
for document in mycol.find().sort("name", -1):
    print(document)


'''
Q7. Explain why delete_one(), delete_many(), and drop() are used.

delete_one(): Deletes a single document that matches the specified criteria.
delete_many(): Deletes all documents that match the specified criteria.
drop(): Deletes an entire collection from the database.
These methods are used to remove data from MongoDB collections. 
delete_one() and delete_many() are used to remove specific documents based on certain conditions, 
while drop() is used to remove an entire collection.
'''