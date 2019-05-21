def repeated_string(s,n):
	count = 0
	index = 0
	num_of_a = 0

	while count < n:
		if index > len(s)-1:
			index = 0
		if s[index] == 'a':
			num_of_a += 1

		count += 1	
		index += 1

	return num_of_a

	# substring = s
	# index = 0

	# while len(substring) < n:
	# 	substring += s
	# 	index += 1

	# if len(substring) > n:
	# 	substring = substring[:n]

	# count = 0
	# for char in substring:
	# 	if char == 'a':
	# 		count += 1

	# return count
print(repeated_string("aba", 10))
print(repeated_string("a",1000000000000))