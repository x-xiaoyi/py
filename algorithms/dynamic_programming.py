"""动态规划入门：爬楼梯（每步可走 1/2/3 阶）。

递推式 ``f(n) = f(n-1) + f(n-2) + f(n-3)``，初值 ``f(0)=1, f(1)=1, f(2)=2``，
原始脚本用滚动变量把它压到 O(1) 空间 —— 思路保留，只补边界和守卫。

用法::

    python algorithms/dynamic_programming.py        # 不带输入时打印 0..10 的结果
    echo 10 | python algorithms/dynamic_programming.py
"""

from __future__ import annotations

import sys


def climb_stairs(steps: int) -> int:
    """返回走完 ``steps`` 阶楼梯的方法数（每步 1、2 或 3 阶）。

    Args:
        steps: 台阶数，``steps >= 0``。

    Returns:
        方法数。``steps == 0`` 返回 1（一步不走也是一种走法）。

    Raises:
        ValueError: ``steps`` 为负数。

    Example:
        >>> [climb_stairs(n) for n in range(6)]
        [1, 1, 2, 4, 7, 13]
    """
    # 修复: 原函数对 n = 0 和负数没有任何处理，会掉进循环外的 return c(=4)，
    #       于是 climb_stairs(0) 返回 4、climb_stairs(-3) 也返回 4，全是错的。
    if steps < 0:
        raise ValueError("steps 不能为负数")
    if steps == 0:
        return 1
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    if steps == 3:
        return 4

    # a, b, c 分别是 f(k-3), f(k-2), f(k-1)
    a, b, c = 1, 2, 4
    for _ in range(4, steps + 1):
        a, b, c = b, c, a + b + c
    return c


def main() -> int:
    """从 stdin 读台阶数；空输入时打印 0..10 的对照表。"""
    raw = sys.stdin.read().strip()
    if not raw:
        print("用法: echo n | python algorithms/dynamic_programming.py")
        print("\nn  ->  climb_stairs(n)")
        for n in range(11):
            print(f"{n:>2}  ->  {climb_stairs(n)}")
        return 0

    try:
        print(climb_stairs(int(raw.split()[0])))
    except ValueError as exc:
        print(f"输入有误: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
