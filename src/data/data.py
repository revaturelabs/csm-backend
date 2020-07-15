''' TODO : docstring documentation '''

import pymongo, os

MONGO_URI_PJ3 = os.getenv('MONGO_URI_PJ3')
mongo = pymongo.MongoClient(MONGO_URI_PJ3)

db = mongo.mongo_csm

if __name__=="__main__":
    pass