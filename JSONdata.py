#working with JSON

import json
from urllib.request import urlopen
"""
objects  - dict
arrays - list
string - str
number(int) - int
number (real) - float
true - True
false - False
null - None

"""
# people_string = """
# {
# 		"people" : [
# 			{ "name": "John Smith",
# 			  "phone" : "111-111-1111",
# 			  "emails" : ["johnsmith@bogusemail.com", "Johns.smith@work-it.com"],
# 			  "has_license" : false
# 			},
# 			{"name" : "Jane Doe",
# 			 "phone" : "222-222-2222",
# 			 "emails" : null,
# 			 "has_license" : true

# 			}
# 		]
# }
# """
# data = json.loads(people_string)
# #print(type(data)) # this will show you the conversion
# #print(data)
# for person in data['people']:
# 	print(person['name'])
# 	del person['phone'] # this will delete the phone number out of the dictionary
# new_string = json.dumps(data, indent=4) #this will dump the post_delete phone number data back into a json and indent each section by 2 spaces.
# print(new_string)

## STATES EXAMPLE

# with open('states.json') as f:
# 	data = json.load(f)
# for state in data['states']:
# 	print(state['name'], state['abbreviation']) # pick a field to use
# 	del state['area_codes']

# 	with open('new_states.json', 'w')as f:
# 		json.dump(data, f, indent=2) 

### API example
with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
 	source = response.read()

#print(source)
data = json.loads(source)
#print(json.dumps(data, indent=2))
#usd_rates = dict()
for item in data['list']['resources']:
	
	name = item['resource']['fields']['name']
	price = item['resource']['fields']['price']
	usd_rates[name] = price

print(50 * float(usd_rates['USD/HTG'])) #this would tell you what 50 HTG dollars would be in US.