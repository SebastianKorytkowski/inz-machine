import datetime
import json
import requests
import time
import psutil

settings = json.load(open('data.json'))
address = "http://" + settings["address"];
id = settings['id']
identityProof = settings['identityProof']

while True:
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    data = {
        "cpuUsage": cpu,
        "ramUsage": ram
    }
    r = requests.post(address + "/logs/machine/" + id, {"jsonData": json.dumps(data), "identityProof":identityProof})
    print(r.content)
    time.sleep(1.0)
