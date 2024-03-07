from flask import Flask, request, jsonify
from instance.config import Config
# import both functions form db.py
from db import get_blogs, save_blog # new


app = Flask(__name__)
app.config.from_object(Config)
blogs = {}

# get blogs
blogs = get_blogs() #new


@app.route("/blogs", methods=['Post'])
def post_method():

    data = request.get_json()
    data['id'] = len(blogs)+1
    data['comments'] = {}
    if data is None:
        return jsonify({'error': 'Invalid JSON data'}), 400  
    save_blog(data)
    # You will need to regress this line by calling save_blog function
    blogs[data['id']]=data #Accessing dictionary item using key. Time space complexity O(1)
 
    return jsonify(blogs), 201

@app.route("/blogs", methods =['GET'])
def get_method():
    return jsonify(blogs), 200

# Where blog_id is the key: blog is the value. And the blog_id is passed in as a integer
@app.route("/blogs/<int:blog_id>/comments", methods = ['POST'])
def add_comments(blog_id):
    comment = request.get_json() #This is data from the user/postman
    if not comment:
        return jsonify({'error':'Invalid JSON data'}), 400

    ## Confirm whether the blog exists
    blog = blogs.get(blog_id)
    if not blog:
        return jsonify({'error': 'blog does not exist'})
    ## If the blog exists add a comment
    comments = blog.get('comments')
    comment_id = comment.get('id')
    comments[comment_id] = comment
    

    ## Return the blog including all the comments
    #update the blogs's comments
    blog['comments'] = comments
    # Save the updated blog data
    save_blog(blog)
    return jsonify({'message': 'Comment added successfully', 'blog':blog}), 201


@app.route("/blogs/<int:blog_id>/comments/<int:comment_id>", methods = ['GET','PUT', 'DELETE'])
def single_comment(blog_id, comment_id):
    # Check if blog exists
    blog = blogs.get(blog_id)
    if not blog:
        return jsonify({'error':'blog does not exist'}), 404
    
    # Retrieve all comments
    comments = blog.get('comments')
    # Check if comment exists 
    comment = comments.get(comment_id)
    if not comment:
        return jsonify({'error':'comment does not exist'}), 404

    # GET method for comments
    if request.method == 'GET':
        return jsonify(comment)
    
    # Delete methods for comment
    if request.method == 'DELETE': 
        del comments[comment_id]
        # Update the comments in the blog data
        blog['comments'] = comments # new
        # Save the updated blog data
        save_blog(blog) # new
        return jsonify({'message':'Comment deleted successfully'}), 200

    # PUT method for comments
    if request.method == 'PUT':
        content_data = request.get_json() #This is data from the user/postman
        if not comment:#consider changing this to content dta
            return jsonify({'error':'Invalid JSON data'}), 400
        comment['content'] = content_data.get('content')
        # Update the comments in log data
        blog['comments']= comments # new
        # save the updated blog
        save_blog(blog) # new
        return jsonify({'message': 'Comment updated successfully'}), 200





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)