from flask import Flask, request, jsonify


app = Flask(__name__)
posts = {}



@app.route("/post", methods=['Post'])
def post_method():

    data = request.get_json()
    data['id'] = len(posts)+1
    if data is None:
        return jsonify({'error': 'Invalid JSON data'}), 400  


    posts[data['id']]=data #Accessing dictionary item using key. time space complexity O(1)
 
    return jsonify(posts), 201

@app.route("/post", methods =['GET'])
def get_method():
    return jsonify(posts), 200

if __name__ == '__main__':
    app.run(debug=True)