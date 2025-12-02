import json

# x = { "ssid":"AndroidAPf08b",
#       "password":"xefa2202"}
with open("passwordFile.pwd") as f:
    x = json.loads(f.read())
print(json.dumps(x))
ssid = x["ssid"]
password = x["password"]
print (ssid)