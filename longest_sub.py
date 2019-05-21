#iterate over string
#create empty set
#check if item is in set
#if not add
#else length = len(set)
#max_length 
#if length > max_length 
#max_length = length
# #set = set()

# "pwwkew"
# [p,w]
# max = 2
# [w,k,e]
# max = 3
# [e,w]
def longest_substring(s):
	current_substring = set()
	max_length = 0

	for char in s:
		if char in current_substring:
			print(current_substring)
			current_substring.add(char)
		else:	
			current_substring.add(char)

		if len(current_substring) > max_length:
			max_length = len(current_substring)


	return max_length
# print(longest_substring("pwwkew"))
# print(longest_substring(" "))
# print(longest_substring("dvdf"))

#variable start = 0
#variable end = 0
#seen = set()
#iterate over s
#if item in seen 
#while s[start] != s[end]
#seen delete start
#start += 1

def longest_sub(s):

	start = 0

	seen = set()

	for char in s:
		if char in seen:
			while s[start] != char:
				# print("this is char",char)
				# print("this is start",s[start])
				seen.remove(s[start])

				start += 1

		else:
			seen.add(char)
		# print(seen,"this is char",char)
	
	return len(seen)
print(longest_sub("pwwkew"))
print(longest_sub(" "))
print(longest_sub("dvdf"))
print(longest_sub("abcabcbb"))

#start = 2
#char = b
#seen = 
#{a,b,c}