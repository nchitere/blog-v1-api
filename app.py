from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {'greeting': 'Hello world!',
            'country' : 'Kenya',
            'gender': 'Male'}

@app.route("/post", methods=['Post', 'Get'])
def post_method():
    if request.method == 'Post':
        data = request.get_json()

        if data is None:
            return jsonify({'error': 'Invalid JSON data'}), 400  # 400 status code indicates a bad request

        # Data handling
        item_id = data.get('id')
        item_name = data.get('item')
        item_price = data.get('price')


    response = ({'id': 444,
            'title':'rice',
            'recipe':'rice curry'})
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)