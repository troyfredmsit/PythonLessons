#Lists, Dictionaries and Tuples/sets
nums = [1,2,3,4,5,6,7,8,9,10]

# # I want 'n' for each 'n' in nums
# my_list = []
# for n in nums:
# 	my_list.append(n)
# print(my_list)

# # short version
# my_list = [n for n in nums]
# print(my_list)

# # I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
# 	my_list.append(n*n)
# print(my_list)

#short version
#my_list = [n*n for n in nums]
#SYNTAX = [What is to be appended(n*n) | forloop ( for n in nums)]


# # using map lambda
# my_list = map(lambda n: n*n,nums)
# #maps memory space
# print(my_list)

#Add to list is n is even
# my_list = []
# for n in nums:
# 	#use NOT for odds
# 	if n%2 == 0:
# 		my_list.append(n)
# print(my_list)

# #short version
# my_list = [n for n in nums if n%2 == 0]
# #SYNTAX [n for n in nums (if statement)]

# # make a pairings for each number letter pair
# my_list = []
# for letter in 'abcd':
# 	for num in range(4):
# 		my_list.append((letter,num))

# print(my_list)
#Short version =[(letter,num) for letter in 'abcd' for num in range(4)]
#print(my_list)

# #Dictionary comprehensions
# names = ['Bruce', 'Clark','Peter','Logan','Wade']
# heros = ['Batman','Superman','Spiderman','Wolverine',"Deadpool"]
# #print names and heros
# print zip(names, heros)
# my_dict = {}
# for name, hero in zip(names,heros):
# 	my_dict[name] = hero
# print(my_dict)

# #short version
# my_dict = {name : hero for name,hero in zip (names,heros)}
# print(my_dict)

# #same but if you wanted to exclude someone
# my_dict = {name : hero for name,hero in zip (names,heros) if name != 'Peter'} # this will allow you to skip over the corrosponding location in each list (aka peter AND spiderman)
# print(my_dict)

# #to exclude all but one.
# my_dict = {name : hero for name,hero in zip (names,heros) if name == 'Peter'} # this will allow you to skip over the corrosponding location in each list (aka peter AND spiderman)
# print(my_dict)

#SETS ARE LIKE LISTS BUT WITH ONLY UNIQUE VALUES
nums = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
# my_set = set()
# for n in nums:
# 	my_set.add(n)
# 	#this will allow only a unique value so the list will kick the duplicates.
# #Short version
my_set = { n for n in nums}
#SYNTAX: Same as dictionaries but without the :
print(my_set)
