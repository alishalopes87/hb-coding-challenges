# Given an array of integers, 
# return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].



def product_exluding(lst, index):
	product = 1
	for num in range(len(lst)):
		if num != index:
			product = product * lst[num] 
	return product

def product_array(lst):

	product_array = []
	for num in range(len(lst)):
		product = product_exluding(lst, num)
		product_array.append(product)

	return product_array

print(product_array([1, 2, 3, 4, 5]))
print(product_array([3, 2, 1]))




