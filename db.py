# comments
# Read and write in a JSON file name blogs.json
# create two functions
# function 1 get blogs
from flask import request
import json
def get_blogs():
    #read blogs.json and return the data
    try:
        with open('blogs.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data
 
# function 2 save blogs
def save_blog(blog:dict):
    # read blogs.json
    # Append the new blog
    blogs = get_blogs()
    next_id = str(len(blogs) + 1)
    blog['id'] = next_id
    blogs[next_id] = blog
    with open('blogs.json', 'w') as file:
        json.dump(blogs, file)

def update_blog(blog:dict):
    blogs = get_blogs()
    blog_id = str(blog.get('id'))
    blogs[blog_id] = blog
    with open('blogs.json', 'w') as file:
        json.dump(blogs, file)

# Make changes to the POST end point
# End point for getting a specific blog


# Delete a blog and update a blog