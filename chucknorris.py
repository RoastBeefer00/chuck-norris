import requests
import json
import random

names = ["Carmen Jasmin", "Bitches", "Fluffets Nuggets"]


response = requests.get("https://api.chucknorris.io/jokes/random")
dump = json.dumps(response.json())
loads = json.loads(dump)
joke = loads["value"]
random_name = random.choice(names)
joke = joke.replace("Chuck Norris",random_name)
print(joke)
