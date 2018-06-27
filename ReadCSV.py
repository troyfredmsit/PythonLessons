import csv

with open('names.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	# for line in csv_reader:
	# 	print(line['email']) # using this we can call the key to get the value


	with open('new_names.csv', 'w') as new_file:
		fieldnames = ['first_name', 'last_name'] # if all fields are wanted ensure they are there
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
		csv_writer.writeheader()
		for line in csv_reader:
			del line['email'] # delete out unwanted lines 
			csv_writer.writerow(line)
##########################################################
	#csv_reader = csv.reader(csv_file)
	#next(csv_reader) # this skips over the first value
#############################################################
	# #this will allow you to form a new delimiter. alsoit will put "" around items containing that delimeter aka smith-johnson will be "simth-johnson"
	# with open('new_names.csv', 'w') as new_file:
	# 	csv_writer = csv.writer(new_file, delimiter ='\t') # delimiter = '-' the \t will make it tabs
	
	# 	for line in csv_reader:
	# 		csv_writer.writerow(line)
#################################################################
# with open('new_names.csv', 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file, delimiter='\t')
# 	#if the delmiter is not a , you need to specify it.
# 	for line in csv_reader:
# 		print(line)