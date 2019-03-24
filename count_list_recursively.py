def count_recursively(lst):
    """Return number of items in a list, using recursion."""

    if not lst:
        return 0

    return 1 + count_recursively(lst[1:])

output = count_recursively([1,2,3])
print(output)