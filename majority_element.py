def majority(nums):
	count = {}
	max_count = 0
	value = nums[0]

	for num in nums:
		count[num] = count.get(num,0) + 1
		print(count[num], "this is max",max_count)
		if count[num] > max_count:
			print("this is count")
			max_count = count[num]
			value = num

	return num 

print(majority([3,2,3]))
print(majority([6,5,5]))