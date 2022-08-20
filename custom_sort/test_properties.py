from hypothesis import given, strategies

from custom_sort.my_sort import my_sort_1, my_sort_2
from custom_sort.my_sort_broken import my_sort_3, my_sort_4, my_sort_5


my_sort = my_sort_2

@given(sample=strategies.lists(strategies.integers()))
def test_deterministic(sample):
    first = my_sort(sample)
    second = my_sort(sample)
    assert first == second


@given(sample=strategies.lists(strategies.integers()))
def test_idempotency(sample):
    once = my_sort(sample)
    twice = my_sort(once)
    assert once == twice


@given(sample=strategies.lists(strategies.integers()))
def test_length_invariance(sample):
    result = my_sort(sample)
    assert len(result) == len(sample)


@given(sample=strategies.lists(strategies.integers()))
def test_is_list(sample):
    result = my_sort(sample)
    assert isinstance(result, list)
    assert hasattr(result, '__iter__')


@given(sample=strategies.lists(strategies.integers()))
def test_pairwise_monotone(sample):
    result = list(my_sort(sample))
    for i, k in zip(result, result[1:]):
        assert i <= k


@given(sample=strategies.lists(strategies.integers()))
def test_preserves_values(sample):
    result = list(my_sort(sample))
    for i in sample:
        assert i in result


@given(sample=strategies.lists(strategies.integers()))
def test_doesnt_insert_values(sample):
    result = list(my_sort(sample))
    for i in result:
        assert i in sample


