#Dictionaries
student = {'name': 'John', 'age': 25, 'courses' : ['Math','CompSci']}
weapons = {'Sword of morning' : [25,10]}
#can use a get to get the value.
#print (student.get('name'))

#to assign a value -->> student['name'] = 'Jane' will change the value.

#to add a totally new value  -->> student['address'] = '1234 some lane.'

#to delete a key pair -->> del student['age']

#popping a value returns the value then deletes it -->> student.pop('age')

#to see how many pairs you have so in the current example the result would be 3 (key pairs)-->> len(students) 

#to see the keys it is student.keys()

#to see the values it is student.values()

#to see all the items it is student.items()

# a way to loop through is to use the keys or values in a for
# for key, value in student.items():
# 	print(key, value)

#to get to  a dictionary value with a list, use it outside of the brackets -->> current_weapon_damage = weapons.get('Sword of morning')[0]
print(weapons.get('Sword of morning')[0])
#to check for values you can do student.get('value', 'what to say if value not found') -->> student('phone','not_found')