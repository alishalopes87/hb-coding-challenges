#subtring =""
#if i = j subtring += i 


def common_prefix(word1,word2):
	subtring = ""
	i = 0
	j = 0

	while i < len(word1) and j < len(word2):
		if word1[i] == word2[j]:
			subtring += word1[i]
			i += 1
			j += 1
		else:
			break

	return subtring

def longest_prefix(array):
	subtring = ""

	if not array:
		return subtring

	if len(array) == 1:
		return array[0]

	word1 = array[0]
	word2 = array[1]
	subtring = common_prefix(word1, word2)

	
	for i in range(2,len(array)):
		subtring = common_prefix(subtring, array[i])

	return subtring





print(longest_prefix(["flower","flow", "flight"]))
print(longest_prefix(["a"]))
#range gives extra control to move indices
