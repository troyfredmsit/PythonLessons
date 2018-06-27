# File objects.


#non context manager method
"""
f = open('test.txt', 'r') # may need pathing if not in same directory, the second variable is what to do (read (r) or write (w) orread/write (r+))

print(f.name) #prints file name
print(f.mode)

f.close() #closes the file
"""
#with open('test.txt', 'r') as f:
	# we work with the file in this block then closes when block ends.
	#this is best practice
	#f_contents = f.read() # whole thing
	#f_contents = f.readlines() #per line as a list
	

#	f_contents = f.readline() # the first line
#	print(f_contents, end='')

#	f_contents = f.readline() # second line
#	print(f_contents, end='')

	#for line in f:
	#	print(line, end='')
	#	#this is the better method to accomplish this
#	size_to_read = 10
#	f_contents = f.read(size_to_read) #this will limit the read to X amount of characters in this case 100
#	while len(f_contents) > 0:
#		print(f_contents, end='*') 
#		f_contents = f.read(size_to_read)

#f.seek(0) #this will go to whatever character you desire.


#print(f.closed) # this allows us to examine properties even after close, but just not read or write.
"""
with open('test2.txt', 'w') as f:
	#this block will write it in succession so TestTest
	#f.write('Test')
	#f.write('Test')

	#this block will seek to 0 and write
	f.write('Test')
	f.seek(0)
	f.write('Test')
"""

#read one file, write to another.
"""
with open('test.txt', 'r') as rf:
	with open('test_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)

#to do this with an image you have to open in binary mode using wb for the write method
with open('iamge1.jpg', 'r') as rf:
	with open('image1_copy.jpg', 'wb') as wf:
		for line in rf:
			wf.write(line)

#to do this with an image you have to open in binary mode using wb for the write method using a chuck size
with open('iamge1.jpg', 'r') as rf:
	with open('image1_copy.jpg', 'wb') as wf:
		chuck_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)
			

"""