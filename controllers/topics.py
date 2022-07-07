import random

# Pokemon_db=[
#     {'id':'1',
#     "pokemon":'Bulbasaur',
#     "type":"grass"},
    
#     {'id':'2',
#     "pokemon":'ivysaur',
#     "type":"grass"},

#     {'id':'3',
#     "pokemon":'Venasuar',
#     "type":"grass"}
# ]


# Articulate_db=[
#     {'People':['King Arthur','Michael Jackson']},
#     {'World':['Paris','The Thames']},
#     {'Nature':['Zebra','Leaf']},
#     {'Object':['Fan','Trident']},
#     {'test':'Fan'},
# ]

# print(Articulate_db[0]) # =people + key
# print(Articulate_db[1]) # =world + key
# print(Articulate_db[0]['People']) # =people value onlye
# print(random.choice(Articulate_db[0]['People'])) # = random people value



Articulate_db1={
    'person':['MJ','King Arthur','Michael Jackson'],
    'world':['Paris','The Thames'],
    'object':['Fan','Trident'],
    'action':['jump','sing'],
    'nature':['Zebra','Leaf'],
}

print('person:', random.choice(Articulate_db1['person'])) 
print('world:', random.choice(Articulate_db1['world']))
print('object:', random.choice(Articulate_db1['object'])) 
print('action:', random.choice(Articulate_db1['action'])) 
print('nature:', random.choice(Articulate_db1['nature'])) 
print('random:', random.choice(Articulate_db1[random.choice(list(Articulate_db1))])) # =random topic/random item








def all(req): 
    return [Articulate_db1], 200

def alltopics(req): 
    return [p for p in Articulate_db1], 200

def person(req): 
    return [p for p in Articulate_db1['person']], 200

def dy(req,usertop): 
    print('here!!!!!!!!!!!!!!!!!!!!!!!!!')
    return [p for p in Articulate_db1[usertop]], 200



# def find_by_uid(uid):
#     try:
#         return next(topic for topic in Articulate_db1 if topic[] == uid)
#     except:
#         raise BadRequest(f"We don't have that cat with id {uid}!")

    cat = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        cat[key] = val
    return cat, 200


# @app.route('/api/Pokemon_db', methods=['GET', 'POST'])
# def Pokemon_db_handler():
#     fns = {
#         'GET': Pokemon_db.index,
#         'POST': Pokemon_db.create
#     }
#     resp, code = fns[request.method](request)
#     return jsonify(resp), code

# @app.route('/api/Pokemon_db/<int:p_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
# def p_handler(p_id):
#     fns = {
#         'GET': Pokemon_db.show,
#         'PATCH': Pokemon_db.update,
#         'PUT': Pokemon_db.update,
#         'DELETE': Pokemon_db.destroy
#     }
#     resp, code = fns[request.method](request, p_id)
#     return jsonify(resp), code

# @app.errorhandler(exceptions.NotFound)
# def handle_404(err):
#     return {'message': f'Oops! {err}'}, 404

# @app.errorhandler(exceptions.BadRequest)
# def handle_400(err):
#     return {'message': f'Oops! {err}'}, 400

# @app.errorhandler(exceptions.InternalServerError)
# def handle_500(err):
#     return {'message': f"It's not you, it's us"}, 500
    