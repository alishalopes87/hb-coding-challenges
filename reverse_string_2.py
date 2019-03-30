# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
# Example:
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Restrictions:
# The string consists of lower English letters only.
# Length of the given string and k will in the range [1, 10000]

def reverseStr(s: str, k: int):
    lst = []
    for i in range(0, len(s), k):
        lst.append(s[i:i+k])

    for item in range(len(lst)):
        if item % k == 0:
            lst[item] = lst[item][::-1]
    return "".join(lst)

output = reverseStr("abcdefg",2)
print(output)