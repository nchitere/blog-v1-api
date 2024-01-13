from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {'greeting': 'Hello world!',
            'country' : 'Kenya',
            'gender': 'Male'}