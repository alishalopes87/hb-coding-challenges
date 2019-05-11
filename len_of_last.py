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

	s_list = s.split(" ")
	length = 0

	for item in s_list:
		if item:
			length = len(item)
	return length


	

print(len_of_last(" this   "))