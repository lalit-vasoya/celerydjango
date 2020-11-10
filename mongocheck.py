import pymongo

client = pymongo.MongoClient("localhost",27017)
db = client.test

movie = db.movie

print(movie)

data = {"name":"abcd3"}
movie.insert_one(data)


data = {"name":"abcd3"}
movie.insert_one(data)

print(movie.count_documents({}))