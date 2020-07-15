''' TODO : docstring documentation '''

import pymongo, os

MONGO_URI = os.getenv('MONGO_URI')
mongo = pymongo.MongoClient(MONGO_URI)

db = mongo.#database_name

if __name__=="__main__":
    