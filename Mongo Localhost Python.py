import pymongo #import the server

client= pymongo.MongoClient('mongodb://localhost:27017/')
#connect with host & 27017 is default port id

db= client ['Oparators'] #connecting to Database


# To see the list of database 

print(client.list_database_names())

for i in client.list_database_names():
    print (i)


#Using the variable to run the program

mongo= client.list_database_names()

for i in mongo:
    print (i)

if 'Movie' in mongo:
    print('Found')


#To check the list of collections


mongo1= db.list_collection_names()

for i in mongo1:
    print(i)


# To get connected to the collection


collection= db['inventory']


#For new collections

New_collection= db['Books']

#To add document in collection

#single document
Var= {
   'code': "xyz",
   'tags': [ "school", "book", "bag", "headphone", "appliance" ],
   'qty': [
          { 'size': "S", 'num': 10, 'color': ["blue","red"] },
          { 'size': "M", 'num': 45, 'color': ["blue","red"] },
          { 'size': "L", 'num': 100, 'color': ["green","red"] }
        ]
}

New_collection.insert_one(Var)

#Many document 


Document=[
{ 'item': { 'name': "ab", 'code': "123" }, 'qty': 15, 'tags': [ "A", "B", "C" ] },
{'item': { 'name': "cd", 'code': "123" },'qty': 20, 'tags': [ "B" ] },
{'item': { 'name': "ij", 'code': "456" }, 'qty': 25, 'tags': [ "A", "B" ] },
{'item': { 'name': "xy", 'code': "456" }, 'qty': 30, 'tags': [ "B", "A" ] },
{'item': { 'name': "mn", 'code': "000" }, 'qty': 20, 'tags': [ [ "A", "B" ], "C" ] }
]


insertMany=New_collection.insert_many(Document)

print(insertMany.inserted_ids)

mongo1= db.list_collection_names()

for i in mongo1:
    print(i)

for i in collection.find():
    print(i)

#Find in collection

#New collection

for i in New_collection.find():
    print(i)

#collection

for i in collection.find():
    print(i)

#conditions to find ()

for i in collection.find ({'item.code':{'$eq':'123'}}):
    print(i)


filter= {'qty':{'$gte':20}}

for i in collection.find (filter):
    print(i)

#delete the Document in collection

#delete One

collection.delete_one({'qty': 30.0})

for i in collection.find ():
    print(i)


#Delete Many (Using Variable option)

deleteMany=collection.delete_many({'qty': 25.0})


#Print count of deleted item

print(deleteMany.deleted_count)

#Update the Document

updMany= collection.update_many({'qty': 15.0},{'$set':{'item.code':'891'}})

print(updMany.modified_count)

for i in collection.find ():
    print(i)


#Update the Document in array

updMany= collection.update_many({'qty': 15.0},{'$addToSet':{'tags':'Z'}})

print(updMany.modified_count)

for i in collection.find ():
    print(i)


