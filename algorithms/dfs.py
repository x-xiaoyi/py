"""全排列（DFS 回溯 / 深度优先 + 剪枝）的参考实现。

原始脚本 dfs.py 在模块顶层直接 ``n = int(input())`` 然后立刻开跑，既没法被测试
导入，也没有任何入参校验。这里把算法收进 ``permutations()``，把交互收进 ``main()``。

用法::

    python algorithms/dfs.py           # 不带输入时用 n=3 演示
    echo 3 | python algorithms/dfs.py
"""

from __future__ import annotations

import sys


def permutations(n: int) -> list[list[int]]:
    """返回 ``1..n`` 的所有全排列，结果按字典序（DFS 的天然顺序）排列。

    Args:
        n: 元素个数，``n >= 0``。

    Returns:
        全排列列表；``n == 0`` 时返回 ``[[]]``（空集合有一种排列）。

    Raises:
        ValueError: ``n`` 为负数。

    Example:
        >>> permutations(2)
        [[1, 2], [2, 1]]
    """
    if n < 0:
        raise ValueError("n 不能为负数")

    results: list[list[int]] = []
    path: list[int] = []
    # 修复: 原脚本用全局 used/path/step，多次调用会互相污染；现在全部收进局部变量。
    used = [False] * (n + 1)  # 下标 1..n 对应数字 1..n

    def backtrack() -> None:
        # 修复: 原代码用 `step` 形参判断终止，但 step 只由调用方 +1 传递，
        #       与 path 长度其实等价；这里直接用 len(path) 判断，语义更直白。
        if len(path) == n:
            results.append(path.copy())  # 修复: 原代码直接 print，无法复用；这里返回副本
            return
        for value in range(1, n + 1):
            if used[value]:
                continue
            used[value] = True
            path.append(value)
            backtrack()
            path.pop()
            used[value] = False

    backtrack()
    return results


def format_permutations(n: int) -> str:
    """把全排列渲染成每行一个 Python 列表，和原始脚本的打印格式一致。"""
    return "\n".join(str(item) for item in permutations(n))


def main() -> int:
    """从 stdin 读 n；空输入时演示 n=3。"""
    data = sys.stdin.read().strip()
    if not data:
        print("用法: echo n | python algorithms/dfs.py")
        print(f"\nn=3 的全部排列（{len(permutations(3))} 个）:")
        print(format_permutations(3))
        return 0

    try:
        n = int(data.split()[0])
        output = format_permutations(n)
    except ValueError as exc:
        # 修复: 原代码 int(input()) 遇到非数字直接抛 ValueError 裸奔到用户面前。
        print(f"输入有误: {exc}", file=sys.stderr)
        return 2

    if output:
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
