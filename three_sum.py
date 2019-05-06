# Write three functions that compute the sum of the numbers 
# in a given list using a for-loop, a while-loop, and recursion.

def sum_for_loop(nums):
	lst_sum = 0

	for i in nums:
		lst_sum += i

	return lst_sum

def sum_while_loop(nums):

	nums_sum = 0
	i = 0

	while i < len(nums):
		nums_sum += nums[i]
		i += 1
	return nums_sum

def recusive_sum(nums):
	if not nums:
		return 0 
	return nums[0] + recusive_sum(nums[1:])

print(sum_for_loop([-5, 10, 4]))
print(sum_while_loop([-5, 10, 4]))
print(recusive_sum([-5, 10, 4]))