import enum
import time
import uuid
from typing import Optional, List, Set

import hypothesis.strategies
import pydantic
from hypothesis import strategies, given, assume
from pydantic import BaseModel, Field


@given(
    number=strategies.integers() | strategies.floats() | strategies.booleans(),
    sequence=strategies.lists(
        strategies.sampled_from(['foo', 'bar']) | strategies.none()
    ),
    text=strategies.text(max_size=10))
def test_show_me_what_u_generate(number, sequence, text):
    print((number, sequence, text))










@given(text=strategies.text())
def test_find_minimal_example(text):
    pass_test = "A" not in text
    print(repr(text), '-->', pass_test)
    assert pass_test










@given(x=strategies.integers(), y=strategies.integers())
def test_detect_flaky_failures(x, y):
    print((x, y))
    assert time.time_ns() % 7 != 1











@given(
    string_working_day=hypothesis.strategies.dates()
        .filter(lambda d: d.weekday() <= 4)  # only Mon-Fri
        .map(lambda d: d.isoformat())  # we want it as strings
        .filter(lambda d: "22" not in d)  # because, why not...
)
def test_filter_map_strategy(string_working_day):
    assume("9" not in string_working_day)

    print(repr(string_working_day))












@given(data=strategies.data())
def test_interactive_drawing(data):
    lower_bound = data.draw(strategies.integers(min_value=0, max_value=10))
    upper_bound = data.draw(strategies.integers(min_value=lower_bound, max_value=10))
    sample = data.draw(strategies.integers(min_value=lower_bound, max_value=upper_bound))

    print(lower_bound, sample, upper_bound)
    assert lower_bound <= sample <= upper_bound













class Skills(enum.Enum):
    pydantic = 1
    pytest = 2
    hypothesis = 3
    asyncio = 4
    magical_meta_programming = 5


class Pythonista(pydantic.BaseModel):
    id: uuid.UUID
    name: str
    age: Optional[int] = Field(..., gt=0, lt=200)
    skills: Set[Skills]


class Meetup:
    def __init__(self, already_signed_up):
        self._signed_up = list(already_signed_up)

    def rsvp(self, member):
        self._signed_up.append(member)

    @property
    def signed_up(self):
        return self._signed_up


@given(
    someone=strategies.from_type(Pythonista),
    initial_visitors=strategies.lists(strategies.from_type(Pythonista)),
)
def test_draw_from_models(initial_visitors, someone):
    assume(someone not in initial_visitors)
    meetup = Meetup(initial_visitors)

    print(someone)
    meetup.rsvp(someone)

    assert someone in meetup.signed_up
