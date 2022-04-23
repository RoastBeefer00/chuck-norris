import requests
import json
import random

names = ["Your Mom", "Chris Olson", "Stan Lee", "Mike Lim"]


response = requests.get("https://api.chucknorris.io/jokes/random")
dump = json.dumps(response.json())
loads = json.loads(dump)
joke = loads["value"]
random_name = random.choice(names)
joke = joke.replace("Chuck Norris",random_name)
print(joke)