from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://adityakshah66:GJU7ErWveUkQYfI0@cluster0.8blwv.mongodb.net/")


db = client.test_database
db = client.scrapy
collection = db.test_collection

post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

post_id  = collection.insert_one(post).inserted_id