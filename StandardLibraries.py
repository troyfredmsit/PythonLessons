print("Import of StandardLibraries.py")

test = 'Test String'

def find_index(to_search, target):
	#find index of a value in a sequence
	for i, value in enumerate(to_search):
		if value == target:
			return 1
	return -1