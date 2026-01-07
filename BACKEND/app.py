from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

accounts = {}

# Serve frontend
@app.route("/")
def home():
    return send_from_directory("../FRONTEND", "index.html")


@app.route("/create", methods=["POST"])
def create_account():
    data = request.json
    name = data["name"]
    balance = int(data["balance"])

    if name in accounts:
        return jsonify({"message": "Account already exists"})

    accounts[name] = balance
    return jsonify({"message": "Account created successfully"})


@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.json
    name = data["name"]
    amount = int(data["amount"])

    if name not in accounts:
        return jsonify({"message": "Account not found"})

    accounts[name] += amount
    return jsonify({
        "message": "Deposit successful",
        "balance": accounts[name]
    })


@app.route("/balance/<name>")
def balance(name):
    if name not in accounts:
        return jsonify({"message": "Account not found"})
    return jsonify({"balance": accounts[name]})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

