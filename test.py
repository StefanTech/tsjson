import json 
print("Starte Lesen Json File")
with open("tsjson/accounts.json") as daten: 
    print(json.dumps(json.load(daten), indent=4))


