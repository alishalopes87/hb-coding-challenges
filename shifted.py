# Given two strings A and B, return whether or not A can be shifted some number of times to get B.

# For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.


def shifted(a,b):
	if len(a) != len(b):
		return False 
	shift = 0

	a = list(a)

	while shift < len(a)-1:
		a.insert(0,a.pop())
		if "".join(a) == b:
			return True
		shift += 1	
	return False

print(shifted('abcde','cdeab'))
print(shifted('abc','acb'))