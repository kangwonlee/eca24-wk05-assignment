'''
Unit tests for one step of the bisction method
The function under test is wk05.wk05()

Would test the following:
1. the binary point is smaller than root
2. the binary point is larger than root
3. both lower end upper bounds are smaller than root
4. both lower end upper bounds are larger than root
'''

import math
import pathlib
import random
import sys

from typing import Callable


import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


sys.path.insert(
    0,
    str(proj_folder)
)


import exercise


random.seed()


@pytest.fixture
def root() -> float:
    return random.uniform(-10, 10)


@pytest.fixture
def f(root:float) -> Callable[[float], float]:
    '''
    Returns an exponential function with a root at the given.
    '''
    a = random.uniform(2.0, 10.0)
    b = -a * math.exp(root)

    def return_this(x:float) -> float:
        return (a * math.exp(x)) + b

    assert math.isclose(return_this(root), 0.0)

    return return_this


@pytest.fixture
def small_epsilon() -> float:
    return 1e-6 * random.uniform(1.0, 9.0)


@pytest.fixture
def big_epsilon() -> float:
    return 1e-1 * random.uniform(1.0, 9.0)


def test__choose_upper__not_found(root:float, f:Callable[[float], float], small_epsilon:float):

    x_next = root + random.uniform(10.0, 5.0)
    assert x_next > root

    delta = random.uniform(20.0, 30.0)

    x_lower = x_next + (-delta)
    x_upper = x_next + delta

    assert math.isclose(abs(x_lower - x_next), abs(x_upper - x_next))
    assert (f(x_lower) * f(x_upper)) < 0

    d = exercise.wk05(f, x_lower, x_upper, epsilon=small_epsilon)

    assert not d['found'], "Please check whether the root found.\n근을 찾은 것이 맞는지 확인 바람."

    assert f(d['x_upper']) * f(d['x_lower']) < 0, "The function values of both two bounds have the same signs. 상한과 하한에서 함수값의 부호가 다르지 않음."

    assert math.isclose(d['x_upper'], x_next), (
        f"Expected `x_upper` to be close to {x_next}, but got {d['x_upper']}\n"
        f"`x_upper` 값이 {x_next} 와 가까울 것으로 예상되었으나, {d['x_upper']} 을(를) 반환함\n"
    )
    assert math.isclose(d['x_lower'], x_lower), (
        f"Expected `x_lower` to be close to {x_lower}, but got {d['x_lower']}\n"
        f"`x_upper` 값이 {x_lower} 와 가까울 것으로 예상되었으나, {d['x_lower']} 을(를) 반환함\n"
    )


def test__choose_lower__not_found(root:float, f:Callable[[float], float], small_epsilon:float):

    x_next = root + random.uniform(-10.0, -5.0)
    assert x_next < root

    delta = random.uniform(20.0, 30.0)

    x_lower = x_next + (-delta)
    x_upper = x_next + delta

    assert math.isclose(abs(x_lower - x_next), abs(x_upper - x_next))
    assert (f(x_lower) * f(x_upper)) < 0

    d = exercise.wk05(f, x_lower, x_upper, epsilon=small_epsilon)

    assert not d['found'], "Please check whether the root found.\n근을 찾은 것이 맞는지 확인 바람."

    assert f(d['x_upper']) * f(d['x_lower']) < 0, "The function values of both two bounds have the same signs. 상한과 하한에서 함수값의 부호가 다르지 않음."

    assert math.isclose(d['x_upper'], x_upper), (
        f"Expected `x_upper` to be close to {x_upper}, but got {d['x_upper']}\n"
        f"`x_upper` 값이 {x_upper} 와 가까울 것으로 예상되었으나, {d['x_upper']} 을(를) 반환함\n"
    )
    assert math.isclose(d['x_lower'], x_next), (
        f"Expected `x_lower` to be close to {x_next}, but got {d['x_lower']}\n"
        f"`x_upper` 값이 {x_next} 와 가까울 것으로 예상되었으나, {d['x_lower']} 을(를) 반환함\n"
    )


def test__choose_upper__found(root:float, f:Callable[[float], float], big_epsilon:float):

    x_next = root + random.uniform(0.05*big_epsilon, 0.1*big_epsilon)
    assert root < x_next

    delta = random.uniform(big_epsilon*0.1, big_epsilon*0.5)

    x_lower = x_next + (-delta)
    x_upper = x_next + delta

    assert x_next < x_upper
    assert x_lower < x_next

    assert root < x_upper
    assert x_lower < root

    assert math.isclose(abs(x_lower - x_next), abs(x_upper - x_next))
    assert (f(x_lower) * f(x_upper)) < 0

    d = exercise.wk05(f, x_lower, x_upper, epsilon=big_epsilon)

    assert d['found'], "Please check whether the root found.\n근을 찾은 것이 맞는지 확인 바람."

    assert f(d['x_upper']) * f(d['x_lower']) < 0, "The function values of both two bounds have the same signs. 상한과 하한에서 함수값의 부호가 다르지 않음."

    assert math.isclose(d['x_upper'], x_next), (
        f"Expected `x_upper` to be close to {x_next}, but got {d['x_upper']}\n"
        f"`x_upper` 값이 {x_next} 와 가까울 것으로 예상되었으나, {d['x_upper']} 을(를) 반환함\n"
    )
    assert math.isclose(d['x_lower'], x_lower), (
        f"Expected `x_lower` to be close to {x_lower}, but got {d['x_lower']}\n"
        f"`x_upper` 값이 {x_lower} 와 가까울 것으로 예상되었으나, {d['x_lower']} 을(를) 반환함\n"
    )


def test__choose_lower__found(root:float, f:Callable[[float], float], big_epsilon:float):

    x_next = root + random.uniform((-0.1)*big_epsilon, (-0.05)*big_epsilon)
    assert x_next < root

    delta = random.uniform(big_epsilon*(0.1), big_epsilon*(0.5))

    x_lower = x_next + (-delta)
    x_upper = x_next + delta

    assert x_next < x_upper
    assert x_lower < x_next

    assert root < x_upper
    assert x_lower < root

    assert math.isclose(abs(x_lower - x_next), abs(x_upper - x_next))
    assert (f(x_lower) * f(x_upper)) < 0

    d = exercise.wk05(f, x_lower, x_upper, epsilon=big_epsilon)

    assert d['found'], "Please check whether the root found.\n근을 찾은 것이 맞는지 확인 바람."

    assert f(d['x_upper']) * f(d['x_lower']) < 0, "The function values of both two bounds have the same signs. 상한과 하한에서 함수값의 부호가 다르지 않음."

    assert math.isclose(d['x_upper'], x_upper), (
        f"Expected `x_upper` to be close to {x_upper}, but got {d['x_upper']}\n"
        f"`x_upper` 값이 {x_upper} 와 가까울 것으로 예상되었으나, {d['x_upper']} 을(를) 반환함\n"
    )
    assert math.isclose(d['x_lower'], x_next), (
        f"Expected `x_lower` to be close to {x_next}, but got {d['x_lower']}\n"
        f"`x_upper` 값이 {x_next} 와 가까울 것으로 예상되었으나, {d['x_lower']} 을(를) 반환함\n"
    )


def test__both_below(root:float, f:Callable[[float], float], small_epsilon:float):
    x_lower = root + random.uniform(-10.0, -6.0)
    x_upper = root + random.uniform(-5.0, -1.0)

    assert x_lower < x_upper

    assert (f(x_lower) * f(x_upper)) > 0

    try:
        d = exercise.wk05(f, x_lower, x_upper, epsilon=small_epsilon)
    except ValueError:
        pass
    else:
        assert False, "Should have raised a ValueError. ValueError 를 발생시켰어야 함."


def test__both_above(root:float, f:Callable[[float], float], small_epsilon:float):
    x_lower = root + random.uniform(1.0, 5.0)
    x_upper = root + random.uniform(6.0, 10.0)

    assert x_lower < x_upper

    assert (f(x_lower) * f(x_upper)) > 0

    try:
        d = exercise.wk05(f, x_lower, x_upper, epsilon=small_epsilon)
    except ValueError:
        pass
    else:
        assert False, "Should have raised a ValueError. ValueError 를 발생시켰어야 함."


if "__main__" == __name__:
    pytest.main([__file__])
