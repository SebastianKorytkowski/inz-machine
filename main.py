import datetime
import json
import requests
import time

settings = json.load(open('data.json'))


while True:
    data = {"timestamp": datetime.datetime.now().isoformat()}
    r = requests.post(settings['address'] + "/logs/machine/" + settings['id'], {"jsonData": json.dumps(data)})
    print(r.content)
    time.sleep(1.0)

