"""自恋数（水仙花数 / Armstrong 数）。

定义：一个 n 位数，若其每位数字的 n 次幂之和等于它本身，则称自恋数。
例：153 = 1³ + 5³ + 3³；9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴。

本文件由三个旧脚本合并而成：

* ``判断水仙花数.py`` —— 有 2 个致命 bug（见下），只保留其"判断某数"的用途；
* ``shuixianhua.py``     —— 同一功能的正确版本（用了 temp 暂存），作为修好的基准；
* ``ceshi.py``           —— 只有 3 行 ``print(shuixianhua(153))`` 的验证脚本，
  其功能并入 ``main()`` 的样例输出。

用法::

    python basics/narcissistic.py       # 打印 0..999 的全部自恋数并复核 153
"""

from __future__ import annotations

# 修复: 原 `判断水仙花数.py` 的实现有两处硬伤，函数永远返回 False 或直接崩溃——
#   1) `s = s + a ** 3` 里 s 从未初始化 -> UnboundLocalError: cannot access local
#      variable 's' where it is not associated with a value；
#   2) 即使把 s 初始化成 0，`while number != 0: number //= 10` 也会把入参除到 0，
#      最后 `if s == number` 等于拿"各位立方和"和 0 比，恒为 False。
#      `shuixianhua.py` 用 temp 暂存原值，这一版就是按它的思路重写的。
#   3) 旧实现把幂次写死成 3，只对三位数成立；这里按位数取幂，符合通用定义。


def is_narcissistic(number: int) -> bool:
    """判断 ``number`` 是否为自恋数。

    Args:
        number: 待判断的整数；负数一律返回 False（自恋数定义在非负整数上）。

    Returns:
        是自恋数返回 True，否则 False。

    Example:
        >>> is_narcissistic(153)
        True
        >>> is_narcissistic(100)
        False
    """
    if number < 0:
        return False
    digits = str(number)  # 不修改入参，从根上避免旧实现"把 number 除到 0"的 bug
    power = len(digits)
    return sum(int(digit) ** power for digit in digits) == number


def find_narcissistic(upper: int, start: int = 0) -> list[int]:
    """返回区间 ``[start, upper)`` 内的全部自恋数。

    Args:
        upper: 上界（不含）。
        start: 下界（含），默认 0。

    Returns:
        升序排列的自恋数列表；区间为空时返回空列表。

    Raises:
        ValueError: ``upper`` 为负数。

    Example:
        >>> find_narcissistic(1000)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
    """
    if upper < 0:
        raise ValueError("upper 不能为负数")
    return [number for number in range(max(0, start), upper) if is_narcissistic(number)]


def main() -> int:
    """打印 0..999 的自恋数，并复核旧脚本 ceshi.py 里那句 ``shuixianhua(153)``。"""
    print("0..999 内的自恋数:", find_narcissistic(1000))
    print(f"153 是自恋数吗? {is_narcissistic(153)}")  # 原 ceshi.py 的输出内容
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
