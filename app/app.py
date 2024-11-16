from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/api")
def hello_json():
    response_data = {
        "organization": "Student Cyber Games",  # Add expected key and value
        "message": "Welcome to the API!",
    }
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
