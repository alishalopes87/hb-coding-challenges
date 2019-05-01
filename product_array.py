# Given an array of integers, 
# return a new array such that each element at index i of the new array 
# is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], 
# the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#create a new empty list
#iterate over input
#create var product
#while len list 
#product = product * (all nums except i)
#append product to new list  

def product_exluding(lst, index):
	product = 1
	for num in range(len(lst)):
		if num != index:
			product = product * num 
	return product

def product_array(lst):

	product_array = []
	for num in range(len(lst)):
		product = product_exluding(lst, num)
		print(product)
		product_array.append(product)

	return product_array

print(product_array([1, 2, 3, 4, 5]))


#look at the list of numbers
#skip number i am on
#multiply next number by all other numbers in list and numbers before skipped
# move on to next number

