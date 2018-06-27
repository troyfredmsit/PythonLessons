#booleans, if and else then.
"""
This is basic if else if and else block
lang = 'Python'

if lang == 'Python':
	print("Language is Python")
elif lang == 'Java':
	print("Language is Java")
else:
	print("No Match")

"""
"""
user = 'Admin'
logged_in = True

# can use or instead of and.
#can use not to flip the natural assumed to False (not logged_in)
if user == 'Admin' and logged_in:
	#in the if statement a varliable will naturally be assumed true
	print('Admin page')
else:
	print("BAD Creds")
	"""

"""
a =[1, 2, 3]
b =[1, 2, 3]

print(a == b) #this is comparing the two objects to see if they equal each other

# this prints out the object ID in memory. They will not be the same unless you put a=b in which case they will take the object ID
# a is b
print(id(a))
print(id(b))
"""
##Things that will show as fals
# False
# None
# Zero of any numeric type
# Any empty sequence '' or () or []
# any empty mapping {}
