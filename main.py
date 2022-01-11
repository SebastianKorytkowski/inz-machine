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

    fulldata = {
        "jsonData": json.dumps(data),
        "identityProof": identityProof
    }
    print("Wysłane dane:")
    print(fulldata)

    r = requests.post(address + "/logs/machine/" + id, fulldata)
    print("Odpowiedź:")
    print(r.content)
    time.sleep(1.0)
