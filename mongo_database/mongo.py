import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://<USER>:<PASSWORD>@<SERVER>/<DATABASE>")
db = client['gump-ia']


def insert(collection, content):
    try:
        doc = db[collection].insert_one(content)
        return doc.inserted_id
    except:
        return None


def update(collection, match, content):
    db[collection].update_one(match, {'$set': content})


def find_one(collection, match):
    try:
        return db[collection].find_one(match)
    except:
        return None


def find(collection, match):
    try:
        return list(db[collection].find(match))
    except:
        return None


def find_all(collection):
    try:
        return list(db[collection].find())
    except:
        return None


def delete(collection, match):
    db[collection].delete_one(match)
