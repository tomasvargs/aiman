from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Datasource API is running!"

@app.route("/api/data")
def get_data():
    return jsonify({
        "status": "success",
        "message": "Dummy response from Azure App Service",
        "data": {
            "id": 1,
            "name": "Sample User",
            "country": "India"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
