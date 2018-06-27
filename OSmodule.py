import os
from datetime import datetime

#print(dir(os)) #This prints out the various modules you can use in it.
print(os.getcwd()) # shows you where you are currently at

#os.chdir('path') # this changes the folder you are in.

#os.mkdir('OS-Demo-2') #this will make a directory in your current folder.
#print(os.listdir())
#os.rmdir('OS-Demo-2') #this will delete the directory user removeddirs(path) for multiple.

#os.rename('test.txt', 'Demo.txt') # will rename files.
#os.stat('demo.txt') # to get data on a file.

#this tells you when something was modified
#mod_time = os.stat('HelloWorld.py').st_mtime
#this puts it into human readable.
#print(datetime.fromtimestamp(mod_time))

"""
for dirpath, dirnames, filenames in os.walk(os.getcwd()):# prints directory, files in the directory and path
	print('Direcotries : ', dirnames)
	print('Current PAth : ' , dirpath) 
	print('Files : ', filenames)
	print()
"""

#this joins to make the path correct
#pathing = os.path.join(os.getcwd,'test.txt')
#print(pathing)
#print(os.environ.get('HOME'))