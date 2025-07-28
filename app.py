from flask import Flask, render_template, jsonify
import boto3
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/api/credentials')
def credentials():
    return jsonify({
        "message": "Credentials retrieved",
        "email": "Person@gmail.com",
        "passcode": "%@PerSon@%"
    })

if __name__ == '__main__':
    app.run(debug=True)
