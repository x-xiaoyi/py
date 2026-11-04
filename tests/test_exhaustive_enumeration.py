"""回文日期枚举的单元测试。"""

from datetime import date

import pytest

from algorithms.exhaustive_enumeration import (
    date_to_digits,
    is_palindrome_date,
    next_palindrome_date,
    parse_day,
)


def test_is_palindrome_date_true_case():
    assert is_palindrome_date(date(2020, 2, 2)) is True


def test_is_palindrome_date_false_case():
    assert is_palindrome_date(date(2020, 2, 3)) is False


def test_date_to_digits_is_zero_padded():
    """修复点回归：年份必须补足 4 位。"""
    assert date_to_digits(date(1, 1, 1)) == "00010101"


def test_date_to_digits_normal_date():
    assert date_to_digits(date(2021, 12, 2)) == "20211202"


def test_next_palindrome_after_known_palindrome():
    """2020-02-02 本身是回文，下一个是 2021-12-02。"""
    assert next_palindrome_date(date(2020, 2, 2)) == date(2021, 12, 2)


def test_next_palindrome_skips_current_day():
    """严格大于起始日：从 2020-02-03 出发也得到 2021-12-02。"""
    assert next_palindrome_date(date(2020, 2, 3)) == date(2021, 12, 2)


def test_next_palindrome_none_within_tiny_window():
    """窗口只有 1 天时找不到下一个回文日期。"""
    assert next_palindrome_date(date(2020, 2, 2), max_days=1) is None


@pytest.mark.parametrize("max_days", [0, -1])
def test_next_palindrome_rejects_non_positive_window(max_days):
    with pytest.raises(ValueError, match="正整数"):
        next_palindrome_date(date(2020, 2, 2), max_days=max_days)


def test_parse_day_compact_format():
    assert parse_day("20200202") == date(2020, 2, 2)


def test_parse_day_dashed_format():
    assert parse_day("2021-12-02") == date(2021, 12, 2)


@pytest.mark.parametrize("text", ["", "2020-2-2", "abcdefgh", "20200230"])
def test_parse_day_rejects_bad_input(text):
    with pytest.raises(ValueError):
        parse_day(text)
