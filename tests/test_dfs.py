"""全排列（DFS 回溯）的单元测试。"""

import pytest

from algorithms.dfs import format_permutations, permutations


def test_permutations_three():
    assert permutations(3) == [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]


def test_permutations_empty_set_has_one_arrangement():
    """n=0 时"什么都不排"也算一种排列。"""
    assert permutations(0) == [[]]


def test_permutations_one_element():
    assert permutations(1) == [[1]]


def test_permutations_count_is_factorial():
    """边界与规模校验：n! 个结果。"""
    assert len(permutations(6)) == 720


def test_permutations_returns_independent_lists():
    """返回的是 path 的副本，改动结果不会污染下一次调用。"""
    first = permutations(2)
    first[0].append(99)
    assert permutations(2) == [[1, 2], [2, 1]]


def test_permutations_rejects_negative():
    with pytest.raises(ValueError, match="负数"):
        permutations(-1)


def test_format_permutations_matches_list_repr():
    assert format_permutations(2) == "[1, 2]\n[2, 1]"
