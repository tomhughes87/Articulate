## THE APP
<br>
players select a category and then are given random words from the api

![image](https://user-images.githubusercontent.com/91187363/178157523-b23b3a6f-2822-4c87-877b-937dd7089738.png)


<hr>
<br>

## Design

![articulate designs](https://user-images.githubusercontent.com/91187363/178157572-b768a5c2-2643-44a1-9189-f6d742cb6647.png)

<hr>
<br>

## run it normally:
- pipenv install
- pipenv shell
- flask run
- http://127.0.0.1:5000 
....anything else? please let me know

or:
- pipenv shell
- pipenv install


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
- *value* = *list* [] of all the words (*string*) belonging to the topic
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


### /
```
The basic game homescreen with btns
```

### /api/all
```
[{"action":["jump","sing","Sit","Save","preserve"],"nature":["Zebra","Leaf","nostril","paws","milk"],"object":["Fan","Trident","Guitar","Bouncy Ball"],"person":["MJ","King Arthur","Michael Jackson","Alfred the Great","Johnny Depp"],"world":["Paris","The Thames","Bangkok","K2","Victoria Falls","Washington","Inverness"]}]
```

### /api/ topics
```
["person","world","object","action","nature"]
```
### /api/ + topic
eg: /api/ person
```
["MJ","King Arthur","Michael Jackson","Alfred the Great","Johnny Depp"]
```
### /api/ + topic/ + int (index)
eg: /api/ person / 1
```
"King Arthur"
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

![image](https://user-images.githubusercontent.com/91187363/178158080-13334f41-d489-4a4a-8fc6-cf43b35a577e.png)

- 12/14 pass
- 98% coverage

<br>

- Failing tests (*fixed*):
    - PATCH
    - CREATE

![image](https://user-images.githubusercontent.com/91187363/178158063-c64ed096-d0a4-4eb8-914b-23840d64e8ef.png)

- Fixed test by Gioele-M

![image](https://user-images.githubusercontent.com/91187363/178240095-2e1b77d3-2006-4a73-8166-7135505ae1ac.png)



<br>
<hr>

## Other
- There are some extra files/folders you can ignore (silly tests, templates, data)
- [Buy the real game on Amazon](https://www.amazon.co.uk/Drumond-Park-Articulate-Family-Board/dp/B00006L99R/ref=sr_1_1_sspa?keywords=articulate+board+games&qid=1657478045&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFPR0M0NThWOFkxMUwmZW5jcnlwdGVkSWQ9QTA5ODMwODYzT0xYWldLS0lVRjJKJmVuY3J5cHRlZEFkSWQ9QTAzMDM3MTkzN1lQNlY0MkZOSFFZJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)
- [See how to play it on YouTube](https://www.youtube.com/watch?time_continue=135&v=xXMsP99edmY&feature=emb_logo)
