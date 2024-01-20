from flask import Flask, request, jsonify
from instance.config import Config


app = Flask(__name__)
app.config.from_object(Config)
blogs = {}



@app.route("/blogs", methods=['Post'])
def post_method():

    data = request.get_json()
    data['id'] = len(blogs)+1
    data['comments'] = []
    if data is None:
        return jsonify({'error': 'Invalid JSON data'}), 400  


    blogs[data['id']]=data #Accessing dictionary item using key. time space complexity O(1)
 
    return jsonify(blogs), 201

@app.route("/blogs", methods =['GET'])
def get_method():
    return jsonify(blogs), 200

if __name__ == '__main__':
    app.run(debug=True)