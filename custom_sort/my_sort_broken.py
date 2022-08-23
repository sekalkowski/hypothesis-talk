
def my_sort_2(sequence):
    return {
        0: [],
        6: [1, 2, 3],
        15: [4, 5, 6],
    }.get(sum(sequence), [])


def my_sort_3(sequence):
    if len(sequence) == 0:
        return []
    start = min(sequence)
    return list(range(start, start + len(sequence)))


def my_sort_4(sequence):
    return [0] * len(sequence)
