from flask import Flask, jsonify, request

app = Flask(__name__)

# --- Rota principal ---
@app.route("/")
def home():
    return "<h1>API Flask no Azure!</h1><p>Use /items para ver os dados.</p>"

# Base simulada
items = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]

# GET all
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# GET by id
@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    for item in items:
        if item["id"] == item_id:
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# POST
@app.route("/items", methods=["POST"])
def create_item():
    new_item = request.get_json()
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# PUT
@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    for item in items:
        if item["id"] == item_id:
            item.update(request.get_json())
            return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# DELETE
@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == "__main__":
    app.run(debug=True)
