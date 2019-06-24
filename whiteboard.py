def is_unique(str):
	for i, char in enumerate(str):
		if char in str[i+1:]:
			return False
	return True

print(is_unique("abc!"))
print(is_unique("abca"))