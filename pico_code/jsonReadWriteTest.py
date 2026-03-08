#jsonReadWriteTest.py
import json

# a Python dictionary object 
x = {
    "name": "Frieda",
    "is_dog": True,
    "hobbies": ["eating", "sleeping", "barking"],
    "age": 8,
    "address": {
        "home": ("Berlin", "Germany") # Tuples are converted to JSON arrays (lists in Python)
    }
}

# convert into JSON:
#y = json.dumps(x)
output_file_path = 'data.json'
with open(output_file_path, 'w') as json_file:
    json.dump(x, json_file)
    
with open('data.json', 'r') as f:
    # Deserialize the file content into a Python dictionary
    data = json.load(f)
        
print (data["name"])

print(data)