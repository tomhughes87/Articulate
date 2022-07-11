import random
import re

Articulate_db={
    'person':['MJ','King Arthur','Michael Jackson','Alfred the Great', 'Johnny Depp'],
    'world':['Paris','The Thames','Bangkok','K2','Victoria Falls', 'Washington','Inverness'],
    'object':['Fan','Trident','Guitar','Bouncy Ball'],
    'action':['jump','sing', 'Sit','Save','preserve'],
    'nature':['Zebra','Leaf','nostril','paws','milk'], 
}

print(Articulate_db)
print('\n\n\n\n\n')
print('the list before', Articulate_db['nature']) 
print('a single word from topics', Articulate_db['nature'][2])
# updatethisword = input('what is you new word?')
# Articulate_db['nature'][2] = updatethisword
print('a edited single word from topics', Articulate_db['nature'][2]) 
print('the list after', Articulate_db['nature'] )


def gen_random_list(req):
    random_list = []
    c=0
    while c in range (10):
        new_random_word = random.choice(Articulate_db[random.choice(list(Articulate_db))])
        if new_random_word in random_list:
            c=c
        else:
            c+=1
            random_list.append(new_random_word)
    sorted(random_list[0])
    return [random_list][0], 200
    
def all(req): 
    return [Articulate_db], 200

def alltopics(req): 
    return [p for p in Articulate_db], 200

def dy(req,usertop): 
    return [p for p in Articulate_db[usertop]], 200

def create(req,usertop):
    new_word = req.get_json()
    Articulate_db[usertop].append(new_word)
    return new_word, 201

def destroy(req,usertop,idx):
    Articulate_db[usertop].remove(Articulate_db[usertop][idx])
    return idx,204

def update(req,usertop,idx):
    Articulate_db[usertop][idx] = req.get_json()
    return idx,204

def getword(req,usertop,idx):
    if [Articulate_db[usertop][idx]] == False:
        return [Articulate_db[usertop][idx]],404
    else:
        return [Articulate_db[usertop][idx]], 200

# def gen_round_list(req,):




# THIS WAS AN OLD DELETE TEST WITH USER INPUT/////////////////
# def checklist(func):
#     def wrapper(*args,**kwargs):
#         print('person:', Articulate_db['person'])
#         func(*args,**kwargs)
#         print('person:', Articulate_db['person'])
#     return wrapper
    
# @checklist
# def delete(del_item):    
#     if del_item in Articulate_db['person']:
#         Articulate_db['person'].remove(del_item),
#         print(del_item,'has been deleted.')
#     else:
#         print(del_item,'is not in the database')
# # delete(input('What do you want to delete?'))
# /////////////////////////////////////