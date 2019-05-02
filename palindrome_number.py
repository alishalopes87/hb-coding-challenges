
# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?

def palindrome_numnber(nums):
	index = 0

	nums = str(nums)

	for num in range(len(nums)-1,-1,-1):
		if nums[num] == nums[index]:
			index += 1
		else:
			return False
	return True

print(palindrome_numnber(121))
print(palindrome_numnber(-121))
print(palindrome_numnber(10))