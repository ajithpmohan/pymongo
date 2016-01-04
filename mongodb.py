from pymongo import MongoClient

client = MongoClient()

#Create DataBase
db = client.mydb

#Create a Collection
collection = db.students

#Insert document into collection
collection.insert({'name':'foo','age':24, 'grade' : 'C'})

#Insert documents into collection
collection.insert_many([{'name':'boo','age':24, 'marks' : 78},
	{'name':'fun', 'marks' : 90, 'grade' : 'C'},
	{'name':'bun','age':27, 'sex':'Male', 'marks' : 48}])

#find documents in a Collection
print 'Query for all documents'
print list(collection.find())
print '\n'

#find document by filtering
q = collection.find({'age':24})
print 'find document by filtering'
for i in q:
	print i
print '\n'

#Logical AND
print 'find operator with AND'
print list(collection.find({'age':24,'marks':78}))
print '\n'

#Logical OR
print 'find operator with OR'
print list(collection.find({'$or':[{'name':'fun'},{'name':'bun'}]}))
print '\n'

#Greater than Operator($gt)
print 'find operator with $gt Operator'
print list(collection.find({'marks':{'$gt':75}}))
print '\n'

#Less than Operator($lt)
print 'find operator with $lt Operator'
print list(collection.find({'marks':{'$lt':75}}))
print '\n'

#update data with pymongo
print 'update_one operator'
r = collection.update_one({'name':'fun'},{'$set':{'grade':'A'}})
print 'matched_count ', r.matched_count
print list(collection.find({'name':'fun'}))
print '\n'

print 'update_one operator with upsert argument'
collection.update_one({'name':'fooo'},{'$set':{'name':'fooo','grade':'B','age':23}},upsert=True)
print list(collection.find({'name':'fooo'}))
print '\n'

#update_many with pymongo
print 'update_many operator'
r = collection.update_many({'age':24},{'$set':{'marks':85}})
print 'matched_count ', r.matched_count
print list(collection.find({'age':24}))
print '\n'

#replace data with pymongo
print 'replace_one operator'
r = collection.replace_one({'name':'bun'},{'name':'booo','marks':60,'grades':'B'})
print list(collection.find())
print '\n'

#delete data with pymongo
print 'delete_one operator'
collection.delete_one({'name':'booo'})
print list(collection.find())
print '\n'

print 'delete_many operator'
r = collection.delete_many({'age':24})
print 'deleted_count ', r.deleted_count
print list(collection.find())
print '\n'

print 'delete_many operator'
r = collection.delete_many({})
print 'deleted_count ', r.deleted_count
print list(collection.find())
print '\n'

#drop a collection
collection.drop()

#drop a database
client.drop_database(db)