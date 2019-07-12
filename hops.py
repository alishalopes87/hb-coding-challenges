# Given an integer list where each number represents the number of hops you can make, 
# determine whether you can reach to the last index starting at index 0.

# For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

def hops(lst):
	hops = 1
	for i in range(len(lst)-1):
		print("current",lst[i])
		hops -= 1
		hops += lst[i]
	if hops <= 0:
		return False
	else:
		return True




print(hops([2, 0, 1, 0]))
print(hops([1, 1, 0, 1]))
print(hops([3,0,0,0]))
print(hops([1, 1, 1, 0]))