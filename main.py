import uvicorn
from fastapi import FastAPI, HTTPException

import crud.db as db
from models.list_item import ListItem

app = FastAPI()


@app.get("/")
def health_check() -> dict:
    return {"health": "ok"}


@app.get("/items")
def get_items():
    res = db.fetch_all_items()
    return res


@app.get("/item/{obj_id}")
def get_item(obj_id: str):
    res = db.fetch_one_item(obj_id)
    if res == None:
        raise HTTPException(status_code=404, detail="No such ID")
    return res


@app.delete("/item")
def delete_item(obj_id: str):
    res = db.delete_item(obj_id)
    if res != "ok":
        raise HTTPException(status_code=404, detail="No such ID")
    return {"status": res}


@app.put("/item")
def update_item(obj_id: str, item: ListItem):
    res = db.update_item(obj_id, item)
    return {"new_object_id": res}


@app.post("/item")
def add_item(item: ListItem):
    res = db.add_item(item)
    return {"new_object_id": res}


if __name__ == "__main__":
    uvicorn.run(app)
