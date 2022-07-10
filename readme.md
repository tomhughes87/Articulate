## THE APP
<br>
players select a category and then are given random words from the api


<hr>
<br>

## run it normally:
- pipenv shell
- flask run
- http://127.0.0.1:5000 
....anything else? please let me know


## running test
from within the pipenv shell:
- pytest --cov-report term-missing --cov=.
- pytest 
- pytest -s (a back-up, use this if using *input()*)

<br>
<hr>

## The Data

<br>

- The DB is a *dictionary*
- *keys* = the topics ''
- *value* = *list* [] of all the words belonging to the category
```
Articulate_db={
    'person':['MJ','King Arthur','Michael Jackson','Alfred the Great', 'Johnny Depp'],
    'world':['Paris','The Thames','Bangkok','K2','Victoria Falls', 'Washington','Inverness'],
    'object':['Fan','Trident','Guitar','Bouncy Ball'],
    'action':['jump','sing', 'Sit','Save','preserve'],
    'nature':['Zebra','Leaf','nostril','paws','milk'], 
}
```

There is another category, *'Random'*. 
- It takes 10 words randomly from the topics
- The random func adds the new words to a blank list 
- a quick check to not allow doubles is performed by converting to a set {} but then back to a list (immutable issus)


<br>
<hr>

## Endpoints

<br>

### /api/all
```
[{"action":["jump","sing","Sit","Save","preserve"],"nature":["Zebra","Leaf","nostril","paws","milk"],"object":["Fan","Trident","Guitar","Bouncy Ball"],"person":["MJ","King Arthur","Michael Jackson","Alfred the Great","Johnny Depp"],"world":["Paris","The Thames","Bangkok","K2","Victoria Falls","Washington","Inverness"]}]
```

### /api/topics
```
["person","world","object","action","nature"]
```
### /api/ <topic>
eg: /api/ person
```
["MJ","King Arthur","Michael Jackson","Alfred the Great","Johnny Depp"]
```

### /api/random
This will be different on every refresh
```
["Paris","Leaf","nostril","King Arthur","Michael Jackson","Sit","preserve","paws","milk","Johnny Depp"]
```


<br>
<hr>

## Testing

<br>

- 10/12 pass
- 98% coverage

- Failing tests:
    - CREATE
    - PATACH



<br>
<hr>

## Other
There are some extra files/folders you can ignore (silly tests, templates, data)