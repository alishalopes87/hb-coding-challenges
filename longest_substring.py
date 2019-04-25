# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, 
#                "pwke" is a subsequence and not a substring.

#iterate over string
#keep track of each characters
#keep going until i see a char i've already subsequence
#save everything before that as a substring
#grab length of that substring save a max_length
#continue and update max_length as you going
#once reached end of string return max_length

def longest_substring(phrase):
    #put substrings into dictionaries
    #key being the length
    #values being substring
    start = 0
    seen = set()
    max_length = 0

    for end in range(len(phrase)):
        print(seen)
        if phrase[end] in seen:
            while phrase[start] != phrase[end]:
                print("start",phrase[start], start, "end",phrase[end],end)
                seen.remove(phrase[start])
                start = start + 1
        else:
            seen.add(phrase[end])
            max_length = max(max_length, len(seen))

    return max_length
print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))
# print(longest_substring(" "))
# print(longest_substring(""))
# print(longest_substring("au"))
# print(longest_substring("dvdf"))
