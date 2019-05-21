def is_palindrome(string):

	for index in range(len(string)//2):
		if string[index] != string[-index -1]:
			return False

	return True

def longest_palidrome(s):
	print(len(s))
	for length in range(len(s),0,-1):
		print(length)
		for index in range(len(s) -length +1):
			temp = s[index: index+ length +1]
			print(temp)
			if is_palindrome(temp):
				return temp
	


print(longest_palidrome("bananas"))