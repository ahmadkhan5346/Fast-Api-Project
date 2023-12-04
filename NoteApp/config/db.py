from pymongo import MongoClient


MONGO_URI = "mongodb+srv://khansarfraz5346:mongodbcompass@clusterpractice.5t0e48z.mongodb.net/notes"

connection = MongoClient(MONGO_URI)