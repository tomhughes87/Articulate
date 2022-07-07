from flask import Flask, render_template, url_for, jsonify, request
from controllers import topics
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/all')
def index():
    fns = {
        'GET': topics.all,
        # 'POST': topics.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code
    
@app.route('/api/topics')
def try1():
    fns = {
        'GET': topics.alltopics,
        # 'POST': topics.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/person')
def try2():
    fns = {
        'GET': topics.person,
        # 'POST': topics.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/<string:usertopic>')
def tryingvar(usertopic):
    print(usertopic)
    
    fns = {
        'GET': topics.dy,
        # 'POST': topics.create
    }
    resp, code = fns[request.method](request,usertopic)
    return jsonify(resp), code


# @app.route('/api/cats/<int:cat_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
# def cat_handler(cat_id):
#     fns = {
#         'GET': topics.show,
#         # 'PATCH': cats.update,
#         # 'PUT': cats.update,
#         # 'DELETE': cats.destroy
#     }
#     resp, code = fns[request.method](request, cat_id)
#     return jsonify(resp), code