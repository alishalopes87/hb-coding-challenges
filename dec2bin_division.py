"""Convert a decimal number to binary representation.

    >>> dec2bin_division(0)
    '0'

    >>> dec2bin_division(1)
    '1'

    >>> dec2bin_division(2)
    '10'

    >>> dec2bin_division(4)
    '100'

    >>> dec2bin_division(15)
    '1111'


"""


def dec2bin_division(num):
    """Convert a decimal number to binary representation."""

    #create an empty result string, result needs to be string or will add binary
    #if num is zero return zero
    #get each value of num % 2
    # concat num % 2 to result
    #update number floor division number

    result = ""

    if num == 0:
        return '0'

    while num >= 1:
        result = (str(num % 2 ) + result)
        num = num // 2

    return result 




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED. W00T!\n")
