# Given a list of strings, find the longest substring of consecutive letters
# and return the longest one. Tie break by alphabetical order
 
# ex:
# input: AAABBBBAABBBCCCCCCCDDAAAAAAAAAADEFGCC
# output: A 10

#declare a var current = string[0]
#declare a var count = 0
#set empty list
#iterate over the string starting at index 1
#compare current to string[i]
#if == increment count
#else current = string[i]
#append current, count to list
#count = 0
#declare var max = list[0][1]
#iterate over list 
#compare tup[1] > max
#max = tup[1]

def longest_substring(string):
	"""
	Args:
		string: str.
	Returns:
		tuple. (str, int)
	"""
	current = string[0]
	count = 0
	# tup_list[i] -> (str, int count)
	tup_list = []
	# populate tup_list
	for char in string[1:]:
		if current == char:
			count += 1 
		else:
			tup_list.append((current, count))
			count = 0

	# compute max of tup_list
	#max_item = compute_max(tup_list)

	best_i = 0
	max_count = tup_list[0][1]
	for i in range(len(tup_list)):
		if tup_list[i][1] > max_count:
			max_count = tup_list[i][1]
			best_i = i
	
	return "{} {}".format(tup_list[best_i][0],tup_list[best_i][1])

print(longest_substring("AAABBBBAABBBCCCCCCCDDAAAAAAAAAADEFGCC"))