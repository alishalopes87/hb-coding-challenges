"""
Write a function that acts like "indexOf", in that it
returns the position of a given string within a
larger string, and returns -1 if the given string
is not found.

Two strings are given as arguments. The first
argument is the smaller string, and the second argument
is the larger string.

Do not use any stdlib string search functions like indexOf, search, index, find,
etc.

Examples:

 str_index_of("Francisco", "San Francisco")
 => 4
 str_index_of("abba", "bbbabbaaa")
 => 3
 str_index_of("Jose", "San Francisco")
 => -1

@param {String} needle
@param {String} haystack
@return integer
"""


def str_index_of(needle, haystack):
    for i in range(len(haystack)):
        found = True
        for j in range(len(needle)):
            if haystack[i+j] != needle[j]:
                found = False

        if found:
            return i
    return -1

print(str_index_of("Francisco", "San Francisco"))
