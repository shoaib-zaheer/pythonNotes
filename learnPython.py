import requests

response = requests.get('https://randomuser.me/api/?results=10')

data = response.json()

for user in data['results']:
  print(user['name']['first']['dob']['age'])
  print(user)