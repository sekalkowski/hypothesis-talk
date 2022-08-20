import time

from hypothesis import strategies, given


@given(
    number=strategies.integers() | strategies.floats() | strategies.booleans(),
    sequence=strategies.lists(
        strategies.sampled_from(['foo', 'bar']) | strategies.none()
    ),
    text=strategies.text(max_size=10))
def test_show_me(number, sequence, text):
    print((number, sequence, text))


@given(text=strategies.text())
def test_find_minimal_example(text):
    pass_test = "A" not in text
    print(text, pass_test)
    assert pass_test


@given(x=strategies.integers(), y=strategies.integers())
def test_detect_flaky(x, y):
    print((x, y))
    assert time.time_ns() % 7 != 1