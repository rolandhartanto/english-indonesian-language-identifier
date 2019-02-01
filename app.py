from dotenv import load_dotenv
load_dotenv()

from flask import Flask
from flask import render_template, request, jsonify
import classify
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/identify", methods=["POST"])
def identify():
    data = json.loads(request.data)
    language = classify.identify_language(data['word'])
    response = {
        "language" : language
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run()