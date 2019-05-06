def is_anagram(test, original):
    test_set = set(test)
    for char in original:
    	print(test_set)
    	print(char)
    	if char in test_set:
    		continue
    	else:
    		return False
    return True 


print((is_anagram('Creative', 'Reactive'), True, 'The word Creative is an anagram of Reactive'))
print((is_anagram("foefet", "toffee"), True, 'The word foefet is an anagram of toffee'))
print((is_anagram("Buckethead", "DeathCubeK"), True, 'The word Buckethead is an anagram of DeathCubeK'))
print((is_anagram("Twoo", "WooT"), True, 'The word Twoo is an anagram of WooT'))
print((is_anagram("dumble", "bumble"), False, 'Characters do not match for test case dumble, bumble'))
print((is_anagram("ound", "round"), False, 'Missing characters for test case ound, round'))
print((is_anagram("apple", "pale"), False, 'Same letters, but different count'))