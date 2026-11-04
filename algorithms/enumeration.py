"""枚举：统计 1..2026 中"各位数字之和为偶数"的整数个数。

题目意图（也是原脚本的意图）：把每个数拆成十进制数字求和，若和为偶数就计数。
原始脚本把计数写在了"逐位累加"的循环体里，于是每算一位就判断一次、符合就 +1，
一个数会被重复计好几次（例如 11：算到 1 时和为 1 奇数，再算到 11 时和为 2 偶数，
只记 1 次；而 22 会被记 2 次）。正确做法是**先把所有位加完，再判断奇偶**。

用法::

    python algorithms/enumeration.py           # 默认统计 1..2026
    echo 1000 | python algorithms/enumeration.py
"""

from __future__ import annotations

import sys

DEFAULT_LIMIT = 2026


def digit_sum(number: int) -> int:
    """返回十进制各位数字之和；负数按绝对值计算。

    Example:
        >>> digit_sum(2026)
        10
    """
    return sum(int(char) for char in str(abs(number)))


def count_even_digit_sum(limit: int = DEFAULT_LIMIT, start: int = 1) -> int:
    """统计闭区间 ``[start, limit]`` 内各位数字之和为偶数的整数个数。

    Args:
        limit: 上界（含）。
        start: 下界（含），默认从 1 开始。

    Returns:
        满足条件的整数个数；区间为空时返回 0。

    Raises:
        ValueError: ``limit`` 或 ``start`` 为负数。

    Example:
        >>> count_even_digit_sum(9)
        4
        >>> count_even_digit_sum(2026)
        1013
    """
    if limit < 0 or start < 0:
        raise ValueError("limit 与 start 不能为负数")

    count = 0
    for number in range(start, limit + 1):
        # 修复: 原代码在 for h in str(i) 的内部就 `if b % 2 == 0: n += 1`，
        #       用"前缀数字和"判断奇偶并重复计数；这里等整数的所有位加完再判断。
        if digit_sum(number) % 2 == 0:
            count += 1
    return count


def main() -> int:
    """从 stdin 读上界；空输入时用默认 2026。"""
    data = sys.stdin.read().strip()
    try:
        # 修复: 原脚本把 2026 写死在 range 里，想换范围只能改代码。
        limit = int(data.split()[0]) if data else DEFAULT_LIMIT
        print(f"1..{limit} 中各位数字之和为偶数的整数个数: {count_even_digit_sum(limit)}")
    except ValueError as exc:
        print(f"输入有误: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
