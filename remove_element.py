# Given an array nums and a value val, 
# remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array,
#  you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. 
# It doesn't matter what you leave beyond the new length.

# Example 1:

# Given nums = [3,2,2,3], val = 3,

# Your function should return length = 2, with the first two elements of nums being 2.

# It doesn't matter what you leave beyond the returned length.

#iterate over nums
#compare each element to val
#if element is equal to val
#replace element with element before it

def remove_element(nums, val):
	"""
	:type nums: List[int]
	:type val: int
	:rtype: int
	"""
	if not nums:
	    return 0
	i = 0
	while i < len(nums):
	    if nums[i] == val:
	        nums.pop(i)
	    else:
	        i += 1
	return len(nums)

print(remove_element([3,2,2,3], 3))
