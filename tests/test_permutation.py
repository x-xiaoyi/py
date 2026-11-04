"""全排列"表格输出"版本的单元测试。"""

import pytest

from algorithms.permutation import format_permutation_table


def test_table_two_elements():
    assert format_permutation_table(2) == ["    1    2", "    2    1"]


def test_table_one_element():
    assert format_permutation_table(1) == ["    1"]


def test_table_zero_elements_prints_nothing():
    """n=0 时没有任何排列要打印，返回空列表。"""
    assert format_permutation_table(0) == []


def test_table_row_count_matches_factorial():
    assert len(format_permutation_table(4)) == 24


def test_table_rejects_negative():
    with pytest.raises(ValueError, match="负数"):
        format_permutation_table(-2)
