"""全排列的"表格输出"入口。

算法本体在 :mod:`algorithms.dfs`（同一份回溯逻辑），本文件只负责把结果按
``f"{i:5d}"`` 的定宽格式排版 —— 也就是原始 permutation.py 的打印样式。
两份回溯代码合并成一份，避免同一道题的两份实现日后各自漂移。

用法::

    python algorithms/permutation.py        # 不带输入时演示 n=3
    echo 3 | python algorithms/permutation.py
"""

from __future__ import annotations

import sys

try:  # 以包方式导入（pytest / python -m algorithms.permutation）
    from algorithms.dfs import permutations as _permutations
except ImportError:  # python algorithms/permutation.py 直跑时 sys.path[0] 是 algorithms/
    from dfs import permutations as _permutations

FIELD_WIDTH = 5


def format_permutation_table(n: int) -> list[str]:
    """返回 n 个数的全排列，每一项是"数字右对齐 5 列"的一行文本。

    Args:
        n: 元素个数，``n >= 0``。

    Returns:
        每个排列一行；``n == 0`` 时返回空列表（空集合不打印任何行）。

    Raises:
        ValueError: ``n`` 为负数。

    Example:
        >>> format_permutation_table(2)
        ['    1    2', '    2    1']
    """
    if n < 0:
        raise ValueError("n 不能为负数")
    # 修复: 原脚本把 `n = int(input())` 放在模块顶层，import 本文件就会卡住等输入，
    #       也没有 `if __name__ == "__main__":` 守卫，无法被测试导入。
    if n == 0:
        return []  # 空集合没有任何一项要排版，返回空列表而不是一个空字符串
    return ["".join(f"{value:{FIELD_WIDTH}d}" for value in item) for item in _permutations(n)]


def main() -> int:
    """从 stdin 读 n；空输入时演示 n=3。"""
    data = sys.stdin.read().strip()
    if not data:
        print("用法: echo n | python algorithms/permutation.py")
        print(f"\nn=3 的全排列表格（{len(format_permutation_table(3))} 行）:")
        for line in format_permutation_table(3):
            print(line)
        return 0

    try:
        n = int(data.split()[0])
        rows = format_permutation_table(n)
    except ValueError as exc:
        print(f"输入有误: {exc}", file=sys.stderr)
        return 2

    # 修复: 原脚本对 n <= 0 直接 raise SystemExit 并打印"请输入一个正整数"，
    #       但 n=0 其实是合法的空排列，这里交给 permutations(0) 返回 [[]] 处理。
    for line in rows:
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
