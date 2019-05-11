#delcare var b = []
#declare i = 0
#delcare j = length a -1
#while i < j 
#b.append(i)
#b.append(j)
# i += 1
#j -= 1
def is_sorted(b):
	#current 
	#if current > current -1
	current = b[0]
	for num in range(1,len(b)):
		if b[num] > current:
			current = b[num]
		else:
			return False

	return True

def generate_array(a):
	b = []
	i = 0
	j = len(a) -1

	while i < j:
		b.append(a[i])
		b.append(a[j])
		i += 1
		j -= 1

	if j == i:
		b.append(a[i])

	return b


def alternating_sort(lst):

	b = generate_array(lst)
	return is_sorted(b)

print(alternating_sort([1,3,5,6,4,2,7]))
print(alternating_sort([1, 3,5,6,4,2]))



