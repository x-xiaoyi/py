"""自恋数（水仙花数）的单元测试。"""

import pytest

from basics.narcissistic import find_narcissistic, is_narcissistic


@pytest.mark.parametrize("number", [153, 370, 371, 407, 1634, 8208, 9474])
def test_known_narcissistic_numbers(number):
    assert is_narcissistic(number) is True


@pytest.mark.parametrize("number", [100, 101, 152, 408, 1635, 9475])
def test_non_narcissistic_numbers(number):
    assert is_narcissistic(number) is False


@pytest.mark.parametrize("number", [0, 1, 9])
def test_single_digit_numbers_are_narcissistic(number):
    """一位数：digit**1 == digit，按通用定义恒成立。"""
    assert is_narcissistic(number) is True


@pytest.mark.parametrize("number", [-1, -153])
def test_negative_numbers_are_not_narcissistic(number):
    assert is_narcissistic(number) is False


def test_find_narcissistic_under_1000():
    assert find_narcissistic(1000) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]


def test_find_narcissistic_small_upper_bound():
    assert find_narcissistic(10) == list(range(10))


def test_find_narcissistic_empty_range():
    """upper == 0 时区间为空。"""
    assert find_narcissistic(0) == []


def test_find_narcissistic_respects_start():
    assert find_narcissistic(1000, start=100) == [153, 370, 371, 407]


def test_find_narcissistic_rejects_negative_upper():
    with pytest.raises(ValueError, match="不能为负数"):
        find_narcissistic(-1)
