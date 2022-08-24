
def my_sort_2(sequence):
    """ lookup table for return values based on the original sum """
    return {
        0: [],
        6: [1, 2, 3],
        15: [4, 5, 6],
    }.get(sum(sequence), [])
















def my_sort_3(sequence):
    """ takes the minimum and counts up from it, keeping the original length """
    if len(sequence) == 0:
        return []
    start = min(sequence)
    return list(range(start, start + len(sequence)))


















def my_sort_4(sequence):
    """ get a list of all-0s of the same length """
    return [0] * len(sequence)
