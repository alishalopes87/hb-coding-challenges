"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    #iterate through list 
    #create variable count 
    #if 0 increment count, if 1 decrement count.

    count = 0
    for branch in branches:
        if branch == 0:
            count += 1
        else:
            count = count - 1

    return count 



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE JUMPING!\n")