
def my_sort_1(sequence):
    if len(sequence) == 0:
        return sequence
    pivot, *rest = sequence
    left = my_sort_1([elem for elem in rest if elem <= pivot])
    right = my_sort_1([elem for elem in rest if elem > pivot])
    return left + [pivot] + right
