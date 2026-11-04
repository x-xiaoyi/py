"""枚举（各位数字和为偶数）的单元测试。"""

import pytest

from algorithms.enumeration import count_even_digit_sum, digit_sum


def test_digit_sum_of_zero():
    assert digit_sum(0) == 0


def test_digit_sum_of_2026():
    assert digit_sum(2026) == 2 + 0 + 2 + 6


def test_digit_sum_uses_absolute_value():
    """负数按绝对值拆位，不会因为 str('-153') 里有个 '-' 崩掉。"""
    assert digit_sum(-153) == 9


def test_count_single_digits():
    """1..9 里只有 2/4/6/8 的数字和是偶数。"""
    assert count_even_digit_sum(9) == 4


def test_count_small_range_known_values():
    """1..10：偶数和的仍是 2/4/6/8 四个（10 的数字和是 1）。"""
    assert count_even_digit_sum(10) == 4


def test_count_up_to_2026():
    """题目要求的主结果：1..2026 共 1013 个。"""
    assert count_even_digit_sum(2026) == 1013


def test_count_up_to_99():
    assert count_even_digit_sum(99) == 49


def test_count_matches_naive_reference_for_small_limit():
    """与"逐个数转字符串再求和"的朴素实现逐项对齐（防止重复计数回归）。"""
    naive = sum(1 for number in range(1, 201) if sum(int(c) for c in str(number)) % 2 == 0)
    assert count_even_digit_sum(200) == naive


def test_count_empty_range_returns_zero():
    """start > limit，区间为空。"""
    assert count_even_digit_sum(10, start=20) == 0


def test_count_zero_limit_returns_zero():
    assert count_even_digit_sum(0) == 0


@pytest.mark.parametrize("limit,start", [(-1, 1), (10, -1)])
def test_count_rejects_negative_bounds(limit, start):
    with pytest.raises(ValueError, match="不能为负数"):
        count_even_digit_sum(limit, start)
