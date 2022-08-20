
def my_sort_1(sequence):
    return list(sorted(sequence))


def my_sort_2(sequence):
    return list(sorted(
        n if isinstance(n, int) else 0 for n in sequence
    ))
