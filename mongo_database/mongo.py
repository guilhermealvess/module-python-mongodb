import pymongo
import os
from dotenv import load_dotenv
load_dotenv()


class Database:

    def __init__(self, database):
        strConn = os.getenv('MONGO_URI')
        client = pymongo.MongoClient(strConn)
        self.__db = client[database]

    def insert(self, collection, document):
        try:
            doc = self.__db[collection].insert_one(document)
            return doc.inserted_id
        except Exception as err:
            return err

    def update(self, collection, match, document):
        try:
            self.__db[collection].update_one(match, {'$set': document})
        except Exception as err:
            return err

    def find_one(self, collection, match=None, fields=None):
        try:
            return self.__db[collection].find_one(match, fields)
        except Exception as err:
            return err

    def find(self, collection, match=None, fields=None):
        try:
            return list(self.__db[collection].find(match, fields))
        except Exception as err:
            return err

    def delete(self, collection, match):
        try:
            self.__db[collection].delete_one(match)
        except Exception as err:
            return err

    def list_collections(self):
        try:
            return self.__db.collection_names()
        except Exception as err:
            return err
