from bson.objectid import ObjectId
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health_check():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"health": "ok"}


def test_get_items():
    res = client.get("/items")
    assert res.status_code == 200


def test_get_item():
    obj_id = ObjectId(b"foo-bar-quux")
    res = client.get(f"/item/{obj_id}")
    assert res.status_code == 404


def test_delete_item():
    obj_id = ObjectId(b"foo-bar-quux")
    params = {"obj_id": str(obj_id)}
    res = client.delete("/item", params=params)
    assert res.status_code == 404
