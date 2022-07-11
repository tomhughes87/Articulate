from crypt import methods
from random import random
from flask import Flask, render_template, url_for, jsonify, request
from flask_cors import CORS
from controllers import topics
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

# ////////////////
# GAME
# ////////////////
@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/nature')
# def game_nature():
#     return render_template('game.html')

# @app.route('/person')
# def game_person():
#     return render_template('game.html')

# @app.route('/world')
# def game_world():
#     return render_template('game.html')

# @app.route('/action')
# def game_action():
#     return render_template('game.html')

# @app.route('/random')
# def game_random():
#     return render_template('game.html')

@app.route('/<string:topic>')
def round_list (topic, methods=['GET']):
    fns = {
        'GET': topics.gen_round_list,
        
    }
    round_db = {}
    c = 0
    while c < 3:
        random.c


    return render_template('game.html', topic_header = topic)

# ////////////////
# API
# ////////////////
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

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's our fault, Sorry"}, 500


if __name__ == "__main__":
    app.run(debug=True)