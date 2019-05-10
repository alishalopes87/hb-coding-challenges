#sum = 0 
# indice = []
#iterate over the with i
#iterate over list with j lst[i:]
#sum = current + lst[i]
#if sum == target
#append i to list
# append j to list
#return list 


def two_sum(lst,target):
	"""
		input: list of integers
		output: list of indices
	"""

	num_sum = 0
	indices = []

	for i in range(len(lst)):

		for j in range(i+1,len(lst)):
			print(lst[j], "this is j" ,j)

			num_sum = lst[i] + lst[j]
			print("this is sum", num_sum)
			if num_sum == target:
				indices.append(i)
				indices.append(j)
				return indices

# print(two_sum([2,7,11,15],9))
# print(two_sum([-5,5],0))
# print(two_sum([-6,-6],-12))

#initialize an empty dict of 
#iterate of list
#if target - lst[i] in dict 
#return [dict[target-list[i]], i]

def two_sum_dict(lst, target):

	values_to_indices = {}

	for num in range(len(lst)):
		if target - lst[num] in values_to_indices:
			return [values_to_indices[target-lst[num]], num]
		else:
			values_to_indices[lst[num]] = num


def find_two_num_sum(lst, total):
   diffs = set()
   for num in lst:
       if num in diffs:
           return [total-num, num]
       else:
           diffs.add(total-num)
   return None

print(find_two_num_sum([7,11,15,2],9))
print(find_two_num_sum([-5,5],0))
print(find_two_num_sum([-6,-6],-12))
# print(two_sum_dict([7,11,15,2],9))
# print(two_sum_dict([-5,5],0))
# print(two_sum_dict([-6,-6],-12))





