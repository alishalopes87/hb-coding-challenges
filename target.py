def two_sum_two_lists(lst1, lst2, target):
    #iterate over both lists
    #for each value see if target - value in lst2
    #if is it return [lst1[i], target - value]

    lst_set = set(lst2)
    for num in lst1:
    	if target - num in lst2:
    		return [target- num, num]

# print(closest_sum([4,5,6],[3,2,5],6))

#closet = target - lst1[0] + lst2[0] 
#iterate over lst1 starting at index 1
#iterate over list1 starting at index 1
# if current_sum = target - lst[i] + lst[j] < closest
# closest = current_sum 
# return closest

def closest_sum(lst1, lst2, target):

	closest = abs(target - (lst1[0] + lst2[0]))

	for i in range(len(lst1)):
		print("this is i",lst1[i])
		for j in range(len(lst2)):
			print("this is j",lst2[j])
			current_sum = abs(target - (lst1[i] + lst2[j]))
			print(current_sum)
			print("this is closest",closest)
			if current_sum < closest:
				closest = current_sum

	return closest

print(closest_sum([1,2,3],[4,5,6],18))