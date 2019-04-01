"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2
"""


def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""

    s = phrase.split(" ")
    count = {}
    results = []

    for word in s:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    for key, value in count.items():
        results.append("{}: {}".format(key, value))

    results = sorted(results)
    for result in results:
        print(result)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
