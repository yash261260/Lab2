from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}


def generate_user_id():
    return max(users.keys()) + 1



@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = generate_user_id()
    new_user = {"name": data["name"], "email": data["email"]}
    users[user_id] = new_user
    return jsonify(new_user), 201


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)



@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user is not None:
        return jsonify(user)
    return "User not found", 404


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = users.get(user_id)
    if user is not None:
        user["name"] = data["name"]
        return jsonify(user)
    return "User not found", 404


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = users.pop(user_id, None)
    if user is not None:
        return "User deleted", 204
    return "User not found", 404


if __name__ == "__main__":
    app.run(port=5000, debug=True)
