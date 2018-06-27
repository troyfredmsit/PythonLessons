"""
#import StandardLibraries as MM allows you to shorten the call so this would be MM.find_index instead of StandardLibraries.find_index.
from StandardLibraries import find_index, test # or * to say everything but frowned upon.
import sys
#this allows you to directly call the function, but limits you to that one function.

#sys.path.append('PAth to the folder') This is how you pick a the folder where your module exists. You can use nano ~/.bash_profile and use export PYTHONPATH="Path to file"
# for windows you can add it to the pathing but seriously lets just .append


# use the as to shorten the name 

# the import statement like this only works if they are in the same directory

courses = ['History', 'Math','Physics', 'CompSci']

#index = StandardLibraries.find_index(courses, 'Math')
# we specify which library we are using then . and then the function unless you shortened it with an as
#index = MM.find_index(courses, 'Math')

index = find_index(courses, 'Math')
#print(index)
#print(test)

print(sys.path) # this lists all the place it will look for these imports
"""
import random
import math
import datetime
import calendar
import os
import antigravity

courses = ['History', 'Math','Physics', 'CompSci']

random_course = random.choice(courses)
#this randomly chooses something from a list in this case the course list.
print(random_course)

#math usage
rads = math.radians(90)
print(math.sin(rads))

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)


