from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder="../frontend/dist", static_url_path="/")
cors = CORS(app, origins="*")


@app.route("/api/users", methods=["GET"])
def users():
    return jsonify({"users": ["Calista", "Carlos", "Charlotte"]})


if __name__ == "__main__":
    app.run(debug=True)
