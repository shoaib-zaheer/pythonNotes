#### pythonNotes
Run python in VScode for first time and some idea running API in python.

[LinkVideo...](https://www.youtube.com/watch?v=W--_EOzdTHk)

* To work with python in vscode, have to make virtual environment to create this we have to use below code in terminal

> $ python3 -m venv python

* Note: it mean we are asking python3 to make virtual `env` by the folder name python.

* No to active this environment use below code in terminal.

> $ source ./python/bin/active

installing plunges for python in vscode `python`, `AREPL for python`, `kite`,

```python
import json

items = json.loads ('[{"id":1,"text": "Item 1"}, {"id":2,"text": "Item 2"}, {"id":3,"text": "Item 3"}]')

for item in items:
  print(item['text'])
```
to install requests extension in python, use below code in terminal.

> $ pip install requests
Now to import API in your python file.
with below we want to generate random users.
```python
import requests

response = requests.get('https://randomuser.me/api')// API
data = response.json()
# json conver this to data
```
To print user first name only

```python
import requests

response = requests.get('https://randomuser.me/api/?results=10')
# get 10 user from api

data = response.json()
# json convert it to readable file

for user in data['results']:
  print(user['name']['first'])
  # for user from data results print first name only
```
