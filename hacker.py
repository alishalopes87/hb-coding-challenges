def AnagramPalindrome(word):

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
print(AnagramPalindrome('carrace'))

def reverseVowels(word):

    #create a set of vowels
    #change string to list because strings are immutable
    #create variables for right that assign to index i
    # variables for left which starts at last item of index string
    #if right in set right = right vowel
    #if left in set , left = left vowel
    # reassign index i to value of left
    # reassign compx_index to value at right

    vowels = {'a','e','i','o','u'}

    string = list(word)
    i = 0
    j = len(word)-1

    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1

    return "".join(string)


output = reverseVowels("hello WORLD")
print(reverseVowels("san francisco"))
print(output)

def nonConsecutiveOnes(num):

    """
        input: num length of bit strings
        output: array of bit strings of that given length that do not contain consecutive ones
        
        >>> n = 3 -> ["000","001","010","101"]
    """
    bits = []

    bits = {'0','1'}

    







