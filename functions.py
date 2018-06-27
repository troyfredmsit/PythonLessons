# FUNCTIONS
"""
# the name = you is how you set a fall back value should a user fail to provide it.
def hello_function(greeting, name = 'You'):
	#pass
	#if we want to leave blank and come back to it later, but not have it break the run use pass
	#print('Hello function!!')
	#return 'Hello Function.'

	#this allows us to use whatever the input variable was to throw into the brackets.
	return '{}, {}'.format(greeting, name)
#using a return we can manipulate the data like .upper() to make it all uppercase.
#print(hello_function().upper())
print(hello_function('Hi')) # this will use default value
print(hello_function('Hi', name = 'Bob')) #this will print using this name instead of default
"""
"""
USING ARGS AND KWARGS FOR POSITONAL UNPACKING
courses = ['Math', 'Art']
info = {'name':'John', 'age': 22}
#to pass these in us * for lists and ** for dictionaries

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)

#the assignment will be the KWARGS where as the straight variables will be the ARGS
student_info('Math', 'Art', name = 'John', age=22)
#This will make associations such as {Name: John, Age:22} where as math and art will make a list AKA (math, art)

student_info(*courses, **info)
#in here the * and ** upacks the values as what they are instead of just however.

student_info(courses, info)
#this will not unpack them right.
"""

"""
FUNCTION IN A FUNCTION
month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
	#return true of leap years, false for non-leapyears
	return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)
	#if the year is divisabel (%) by 4 and the year is not divisable by 100 or is divisable by 400

def days_in_month(year, month):
	#return number of days in theat month in that year

	if not 1<= month <= 12:
		#checks if the month is invalid aka not 1-12
		return 'Invalid month'
	if month == 2 and is_leap(year):
		#is_leap is our above function returning either true or false
		#is it month 2 (feb)
		return 29
	return month_days[month]

#print(is_leap(2020))
print(days_in_month(2017,2)) # 2017 is not leap but 2020 is.
"""