import pytest

from custom_sort.my_sort import my_sort_1
from custom_sort.my_sort_broken import my_sort_2, my_sort_3, my_sort_4

my_sort = my_sort_1
# my_sort = my_sort_2  # oh no!
# my_sort = my_sort_3  # oh damn, please, no!
# my_sort = my_sort_4  # we'll look at this later ;-)



def test_my_sort_minimally():
    sample = [1, 3, 2]
    expected = [1, 2, 3]
    assert my_sort(sample) == expected















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
