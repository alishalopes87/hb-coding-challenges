"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    #if letter in the word has a partner it is 
    #if one extra that's ok
    #iterate over the word 
    #see if i in the rest of the word continue
    # if it is not in rest of word increase count
    #if count is > 1 return false

    count = {}
    if len(word) == 2 and word[0] != word[1]:
        return False

    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    odd = 0
    for char in count:
        if count[char] % 2 != 0:
            odd += 1
        if odd > 1:
            return False
        

    return True
            


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
