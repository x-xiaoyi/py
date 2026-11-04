"""爬楼梯动态规划的单元测试。"""

import pytest

from algorithms.dynamic_programming import climb_stairs


@pytest.mark.parametrize(
    "steps,expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 4),
        (4, 7),
        (5, 13),
        (10, 274),
    ],
)
def test_climb_stairs_known_values(steps, expected):
    assert climb_stairs(steps) == expected


def test_climb_stairs_zero_is_one_way():
    """边界回归：旧实现在 n<=0 时错误地返回 4。"""
    assert climb_stairs(0) == 1


@pytest.mark.parametrize("steps", [-1, -5])
def test_climb_stairs_rejects_negative(steps):
    with pytest.raises(ValueError, match="负数"):
        climb_stairs(steps)


def test_climb_stairs_matches_brute_force():
    """与"枚举走法数"的递推定义逐项对照。"""

    def brute(n: int) -> int:
        if n == 0:
            return 1
        total = 0
        for step in (1, 2, 3):
            if n - step >= 0:
                total += brute(n - step)
        return total

    assert [climb_stairs(n) for n in range(9)] == [brute(n) for n in range(9)]
