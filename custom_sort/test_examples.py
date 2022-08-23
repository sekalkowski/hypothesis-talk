import pytest

from custom_sort.my_sort import my_sort_1
from custom_sort.my_sort_broken import my_sort_2, my_sort_3

my_sort = my_sort_1


def test_my_sort_minimally():
    assert my_sort([1, 3, 2]) == [1, 2, 3]


@pytest.mark.parametrize(("sample", "expected"), [
    ([1, 2, 3], [1, 2, 3]),
    ([1, 3, 2], [1, 2, 3]),
    ([3, 2, 1], [1, 2, 3]),
    ([6, 5, 4], [4, 5, 6]),
    ([], []),
])
def test_my_sort(sample, expected):
    assert my_sort(sample) == expected


@pytest.mark.parametrize("sample", [
    [1, None],
    [1, "foo"],
    [0, [0]],
])
def test_raises_type_error_for_weird_stuff(sample):
    with pytest.raises(TypeError):
        my_sort(sample)
