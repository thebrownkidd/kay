import json
import os

temp = {}
filloc = {
    "update kr na" : "bruh"
}

if os.path.exists("filloc.json"):
    with open("filloc.json", "r") as f:
        temp = json.load(f)

for key,value in filloc:
    temp[key] = value
    
print(temp)

with open ("filloc.josn","w") as f:
    json.dump(temp,f)
