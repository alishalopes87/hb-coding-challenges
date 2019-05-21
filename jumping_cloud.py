def jumpingOnClouds(c):
	jumps = 0
	position = 0

	while position < len(c)-1:
		print("this is position", position)
		if position + 2 < len(c) and c[position + 2] == 0:
			position += 2
		else:
			position += 1
		jumps += 1

	return jumps

print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 0, 0, 1, 0,0]))

#iterate over list
#if index + 2 < len(c) and if c[index] == 0:
#else
#index = index + 1


