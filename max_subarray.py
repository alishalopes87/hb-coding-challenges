# Given an integer array nums, find the contiguous subarray (
# containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, 
# try coding another solution using the divide and conquer approach, which 
# is more subtle.

#initialize max sum = 0
#intialize sum = 0
#initialize variable at list[0]
#iterate over list adding to sum
# if sum > max_sum max_sum = som
#sum = 0
#return max_sum

def max_subarray(nums):
	max_sum = nums[0]
	prev = nums[0]

	for i in nums[1:]:
		if prev > 0:
			prev += nums[i]
		else:
			prev = nums[i]

		max_sum = max(max_sum, prev)
	return max_sum

print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))