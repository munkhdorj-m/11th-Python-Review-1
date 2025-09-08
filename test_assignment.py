import pytest
from assignment import last_digit_even_or_odd, check_positive_negative, has_even_digits, largest_digit, second_last_digit_is_5

@pytest.mark.parametrize("num, expected", [
    (123, "Odd"),
    (246, "Even"),
    (0, "Even"),
    (57, "Odd"),
    (82, "Even")
])
def test1(num, expected):
    assert last_digit_even_or_odd(num) == expected

@pytest.mark.parametrize("num, expected", [
    (10, "Positive"),
    (-5, "Negative"),
    (0, "Neither"),
    (100, "Positive"),
    (-1, "Negative")
])
def test2(num, expected):
    assert check_positive_negative(num) == expected

@pytest.mark.parametrize("num, expected", [
    (1234, True),
    (567, False),
    (89, True),
    (7, False),
    (1000, True)
])
def test3(num, expected):
    assert has_even_digits(num) == expected

@pytest.mark.parametrize("num, expected", [
    (472, 7),
    (1059, 9),
    (333, 3),
    (9081, 9),
    (560, 6)
])
def test4(num, expected):
    assert largest_digit(num) == expected

@pytest.mark.parametrize("num, expected", [
    (157, True),
    (432, False),
    (5, False),
    (105, True),
    (99, False)
])
def test5(num, expected):
    assert second_last_digit_is_5(num) == expected
