# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
#return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5

#split string in list
#get last item of list
#return length

def len_of_last(s):
	"""
		input: str
		output: int
	"""

	count = 0
	local_count = 0

	for i in range(len(s)):
		if s[i] == ' ':
			local_count = 0
		else:
			local_count += 1
			count = local_count
	return count

print(len_of_last("Hello World"))
print(len_of_last("a "))
print(len_of_last(""))
print(len_of_last(" "))
