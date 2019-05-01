# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?

def sum_to_k(lst, k):

	for num in range(len(lst)):
		if k - num in lst:
			return True 
	return False


output = sum_to_k([10, 15, 3, 7], 17)
print(output)
output = sum_to_k([5,3,8,12],40)
print(output)