from flask import Flask, render_template, url_for, jsonify, request
from flask_cors import CORS
from controllers import topics
# from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/random')
def random_api():
    fns = {
        'GET': topics.gen_random_list,
        
    }
    resp, code = fns[request.method](request)    
    return jsonify(resp), code

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

@app.route('/api/<string:usertopic>',  methods=['GET', 'POST', 'DELETE'])
def tryingvar(usertopic):
    print(usertopic)
    
    fns = {
        'GET': topics.dy,
        'POST': topics.create,
        # 'PATCH': topics.update,
    }
    resp, code = fns[request.method](request,usertopic)
    return jsonify(resp), code


@app.route('/api/<string:usertopic>/<int:idx>', methods=['GET','DELETE', 'PATCH'])
def indexword(usertopic,idx):
    fns = {
        'GET':topics.getword,
        'DELETE': topics.destroy,
        'PATCH': topics.update,
    }
    resp, code = fns[request.method](request,usertopic,idx)
    return jsonify(resp), code

if __name__ == "__main__":
    app.run(debug=True)