def bubble_sort(lst):
    """Basic bubble sort."""

    for i in range(len(lst) - 1):
        print("this is i" , i)
        for j in range(len(lst) - 1):
            print("this is j",j)
            if lst[j] > lst[j + 1]:
                # Pair out-of-order, swap them
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

bubble_sort([6, 5, 3, 1, 8, 7, 2, 4])