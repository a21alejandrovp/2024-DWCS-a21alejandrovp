################################
# Transform json as a string --->> Python object
import json
json_string = '{"name": "Alice", "age": 25}'
data = json.loads(json_string)  # Parses the JSON string
print(data)

################################
# Transform json from a file ---> Python object
import json
try:
	file = open('data.json', 'r')
	catalog = json.load(file)   # json.loads(file.read())
except:
	print("error")
finally:
	file.close()
	
##############################
# Transform json from a file ---> Python object
with open('data.json', 'r') as file:
	catalog = json.load(file)
	
	
	
	
	
	
	
	
