from fastapi import FastAPI, HTTPException

app = FastAPI()

items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
def create_item(new_item: dict):
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: dict):
    for item in items:
        if item["id"] == item_id:
            item.update(updated_item)
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    items = [item for item in items if item["id"] != item_id]
    return {"message": "Item deleted"}
