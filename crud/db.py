import os

from bson.errors import InvalidId
from bson.objectid import ObjectId
from models.list_item import ListItem
from pymongo import MongoClient

MONGO_URL = os.environ.get("MONGO_URL")

client = MongoClient(MONGO_URL)
db = client.get_database("TodoList")
coll = db.get_collection("Items")


def doc_helper(item: dict) -> dict:
    item["Id"] = str(item.pop("_id"))
    return item


def fetch_all_items() -> list:
    res = [doc_helper(item) for item in coll.find()]
    return res


def fetch_one_item(obj_id: str) -> dict:
    try:
        res = coll.find_one({"_id": ObjectId(obj_id)})
    except InvalidId:
        res = None

    if res == None:
        return res
    return doc_helper(res)


def add_item(item: ListItem) -> str:
    res = coll.insert_one(item.dict())
    return str(res.inserted_id)


def update_item(obj_id: str, item: ListItem) -> str:
    res = coll.replace_one({"_id": ObjectId(obj_id)}, item.json())
    return str(res.upserted_id)


def delete_item(obj_id: str) -> str:
    try:
        res = coll.delete_one({"_id": ObjectId(obj_id)})
        if res.deleted_count == 0:
            return None
    except InvalidId:
        return None
    return "ok"
