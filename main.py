import datetime
import json
import requests
import time

settings = json.load(open('data.json'))
address = "http://" + settings["address"];
id = settings['id']
identityProof = settings['identityProof']

while True:
    data = {"timestamp": datetime.datetime.now().isoformat()}
    r = requests.post(address + "/logs/machine/" + id, {"jsonData": json.dumps(data), "identityProof":identityProof})
    print(r.content)
    time.sleep(1.0)
