# Modules
from flask import Flask, request
import psycopg2
import secrets

# Intialization
app = Flask(__name__) 

# Connect to the database 
conn = psycopg2.connect(
    database='postgres',
    user='postgres', 
	password='password',
    host='localhost',
    port='5432'
) 
cur = conn.cursor()

# ------------------- Function Section -------------------
# Function sendResult - returns a custom response for an API call
def sendResult(code, result):
    return {
        'code': code,
        'result': result
    }

# Function sendError - returns a standard error code with a message
def sendError(err):
    print(err)
    return {
        'code': 500,
        'error' : err
    }

# Function checkToken - does checking of the existence of a token
def checkToken(token):
    if not token:
        return False
    return True
# ------------------- End Function Section -------------------

# ------------------- API Section -------------------
# API users - returns all users from the users table, including username, displayname, and id
@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        cur.execute('SELECT username, displayname, id FROM users;')
        users = cur.fetchall()

        return sendResult(200, users)
    except psycopg2.Error as err:
        return sendError(err)

# API createUser - creates a user based on username, displayname, and password 
@app.route('/users/createUser', methods=['POST'])
def create_user():
    username = request.form['username']
    displayname = request.form['displayname']
    password = request.form['password']

    try:
        cur.execute('INSERT INTO users (username, displayname, password) VALUES (%s, %s, %s) RETURNING id;', (username, displayname, password))
        userId = cur.fetchone()

        conn.commit()

        return sendResult(201, userId)
    except psycopg2.Error as err:
        return sendError(err)
    
# API deleteUser - deletes a user based on userID
@app.route('/users/deleteUser', methods=['DELETE'])
def delete_user():
    userId = request.form['userid']

    try:
        cur.execute('DELETE FROM users WHERE id = %s;', (userId,))
        conn.commit()

        return sendResult(200, 'deleted')
    except psycopg2.Error as err:
        return sendError(err)

# API login - attempts user login with username and password; returns a token if successful
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    try:
        cur.execute('SELECT * FROM users WHERE username = %s;', (username,))
        user = cur.fetchone()

        if user is None or password != user[2]:
            return sendResult(404, 'Incorrect credentials')
        else:
            token = secrets.token_hex()
            return sendResult(200, [ user[3], token ])
    except psycopg2.Error as err:
        return sendError(err)

# API posts - returns all posts from the posts table, including postID, title, body, userID, and edited
@app.route('/posts', methods=['GET'])
def get_all_posts():
    try:
        cur.execute('SELECT * FROM posts;')
        posts = cur.fetchall()

        return sendResult(200, posts)
    except psycopg2.Error as err:
        return sendError(err)

# API getPost - finds a post using the postID
@app.route('/posts/getPost', methods=['GET'])
def get_post():
    postId = request.form['id']

    try:
        cur.execute('SELECT * FROM posts WHERE id = %s;', (postId,))
        post = cur.fetchone()

        return sendResult(200, post)
    except psycopg2.Error as err:
        return sendError(err)

# API createPost - creates a post based on userID, title, and body
@app.route('/posts/createPost', methods=['POST'])
def create_post():
    userId = request.form['userid']
    title = request.form['title']
    body = request.form['body']
    token = request.headers.get('Authorization')

    if not checkToken(token):
        return sendResult(403, 'Missing token')
    
    try:
        cur.execute('INSERT INTO posts (title, body, userid) VALUES (%s, %s, %s) RETURNING id;', (title, body, userId))
        postId = cur.fetchone()

        conn.commit()

        return sendResult(200, postId)
    except psycopg2.Error as err:
        return sendError(err)

# API updatePost - updates an existing post based on postID, title, and body
@app.route('/posts/updatePost', methods=['PUT'])
def update_post():
    postId = request.form['postid']
    title = request.form['title']
    body = request.form['body']
    token = request.headers.get('Authorization')

    if not checkToken(token):
        return sendResult(403, 'Missing token')
    
    try:
        cur.execute('UPDATE posts SET title = %s, body = %s, edited = TRUE WHERE id = %s;', (title, body, postId))
        conn.commit()

        return sendResult(200, 'updated')
    except psycopg2.Error as err:
        return sendError(err) 

# API deletePost - deletes an existing post based on postID
@app.route('/posts/deletePost', methods=['DELETE'])
def delete_post():
    postId = request.form['postid']
    token = request.headers.get('Authorization')

    if not checkToken(token):
        return sendResult(403, 'Missing token')

    try:
        cur.execute('DELETE FROM posts WHERE id = %s;', (postId,))
        conn.commit()

        return sendResult(200, 'deleted')
    except psycopg2.Error as err:
        return sendError(err) 
# ------------------- End API Section -------------------   
