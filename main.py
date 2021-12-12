import json
import requests

settings = json.load(open('data.json'))
r = requests.get(settings['address'])

print(r.content)