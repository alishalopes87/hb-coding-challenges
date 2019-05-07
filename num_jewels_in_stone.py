# You're given strings J representing the types of stones that are jewels, 
# and S representing the stones you have.  
# Each character in S is a type of stone you have.  
# You want to know how many of the stones you have are also jewels.

# The letters in J are guaranteed distinct, 
# and all characters in J and S are letters. 
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:

# Input: J = "z", S = "ZZ"
# Output: 0
# Note:

# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.

#iterate over J
#add each element to dict
#iterate over s
#increment value of elem in j based on a
#create sum var
#iterate over keys in dict adding to sum
#return sum 
def num_jewels_in_stone(J,S):

	stones = {}

	for stone in S:
		if stone in stones:
			stones[stone] += 1
		else:
			stones[stone] = 1

	total_jewels = 0

	for jewel in J:
		if jewel in stones:
			total_jewels += stones[jewel]

	return total_jewels

print(num_jewels_in_stone("aA","aAAbbbb"))
print(num_jewels_in_stone("z","ZZ"))
