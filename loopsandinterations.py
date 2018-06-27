nums = [1, 2, 3, 4, 5]
"""
for num in nums:
	if num == 3:
		print("Found!")
		#the break will take us out of the loop
		#break

		#the continue will start the next iteration instead of pressing on so in this case it prints found at number 3 then starts the next loop to 4
		continue
	print(num)

"""

"""
for num in nums:
	#nested loop will loop through each num AND each letter in the abc so 1a 1b 1c etc
	for letter in 'abc':
		print(num, letter)
"""
"""
for i in range(1, 11):
	#for the range numbers start at 0 so a range of 10 is number 0-9, to start at a certain number u put number , range (so 1, 11 for 1-10)
	print(i)
"""

#WHILE LOOP#
x = 0

while x < 10:
	print(x)
	x += 1