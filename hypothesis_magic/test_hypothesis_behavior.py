import enum
import time
import uuid
from typing import Optional, Set

import hypothesis.strategies
import pydantic
from hypothesis import strategies, given, assume
from pydantic import Field


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
)
def test_filter_map_strategy(string_working_day):
    assume("9" not in string_working_day)

    print(repr(string_working_day))












@given(interactive_strategy=strategies.data())
def test_interactive_sampling(interactive_strategy):
    lower_bound = interactive_strategy.draw(strategies.integers())
    upper_bound = interactive_strategy.draw(strategies.integers(min_value=lower_bound))
    in_between = interactive_strategy.draw(strategies.integers(min_value=lower_bound, max_value=upper_bound))

    print(lower_bound, in_between, upper_bound)
    assert lower_bound <= in_between <= upper_bound













class Skills(enum.Enum):
    pydantic = 1
    pytest = 2
    hypothesis = 3
    static_code_analysis = 4
    asyncio = 5
    magical_meta_programming = 6


class Pythonista(pydantic.BaseModel):
    id: uuid.UUID
    name: str
    age: Optional[int] = Field(..., gt=0, lt=200)
    skills: Set[Skills] = Field(description="Very particular set of skills")


class Meetup:
    def __init__(self, already_signed_up):
        self._signed_up = list(already_signed_up)

    def rsvp(self, member):
        self._signed_up.append(member)

    @property
    def reservations(self) -> int:
        return len(self._signed_up)


@given(
    someone=strategies.from_type(Pythonista),
    initial_visitors=strategies.lists(strategies.from_type(Pythonista)),
)
def test_draw_from_models(initial_visitors, someone):
    meetup = Meetup(initial_visitors)
    before = meetup.reservations

    print(someone)
    meetup.rsvp(someone)

    assert meetup.reservations == before + 1
