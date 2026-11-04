"""枚举（穷举）：找出指定日期之后的第一个"回文日期"。

回文日期指 ``yyyymmdd`` 这 8 位数字左右对称，例如 2020-02-02 -> 20200202。

原始脚本从 2020-02-02 起一天一天往后试，最多试 5000 天。把它拆成
``is_palindrome_date()`` / ``next_palindrome_date()`` 之后既可测试也便于复用。

用法::

    python algorithms/exhaustive_enumeration.py            # 默认从 20200202 往后找
    echo 20211202 | python algorithms/exhaustive_enumeration.py
"""

from __future__ import annotations

import sys
from datetime import date, timedelta

DATE_FORMAT = "%Y%m%d"
DEFAULT_START = "20200202"
DEFAULT_MAX_DAYS = 5000


def date_to_digits(day: date) -> str:
    """把日期格式化为 ``yyyymmdd`` 八位字符串。

    修复: 原代码用 ``strftime('%Y%m%d')``，``%Y`` 不保证补零到 4 位
    （部分平台把公元 1 年输出成 ``1``），会让 1000 年以前的回文日期判断失败。
    这里手写 ``{year:04d}`` 保证定长。
    """
    return f"{day.year:04d}{day.month:02d}{day.day:02d}"


def is_palindrome_date(day: date) -> bool:
    """判断 ``day`` 的 ``yyyymmdd`` 写法是否回文。

    Example:
        >>> is_palindrome_date(date(2020, 2, 2))
        True
    """
    text = date_to_digits(day)
    return text == text[::-1]


def next_palindrome_date(start: date, max_days: int = DEFAULT_MAX_DAYS) -> date | None:
    """返回 ``start`` 之后（严格大于）的第一个回文日期。

    Args:
        start: 起始日期，本身是否回文不影响结果。
        max_days: 最多向后穷举多少天，必须是正整数。

    Returns:
        找到的回文日期；窗口内没有则返回 None。

    Raises:
        ValueError: ``max_days`` 非正。

    Example:
        >>> next_palindrome_date(date(2020, 2, 2))
        datetime.date(2021, 12, 2)
    """
    if max_days <= 0:
        raise ValueError("max_days 必须是正整数")

    current = start
    for _ in range(max_days):
        current += timedelta(days=1)
        if is_palindrome_date(current):
            return current
    return None


def parse_day(text: str) -> date:
    """解析 ``yyyymmdd`` 或 ``yyyy-mm-dd``。

    Raises:
        ValueError: 无法解析为合法日期。
    """
    cleaned = text.strip().replace("-", "")
    if len(cleaned) != 8 or not cleaned.isdigit():
        raise ValueError(f"无法解析日期 {text!r}，请用 yyyymmdd 或 yyyy-mm-dd")
    try:
        return date(int(cleaned[:4]), int(cleaned[4:6]), int(cleaned[6:]))
    except ValueError as exc:
        raise ValueError(f"{text!r} 不是合法日期: {exc}") from exc


def main() -> int:
    """从 stdin 读起始日期；空输入时用 20200202。"""
    raw = sys.stdin.read().strip()
    try:
        # 修复: 原脚本把起始日期和 5000 天窗口都写死在代码里，且 parse 失败会
        #       直接把 traceback 甩给用户。
        start = parse_day(raw) if raw else parse_day(DEFAULT_START)
        found = next_palindrome_date(start, DEFAULT_MAX_DAYS)
    except ValueError as exc:
        print(f"输入有误: {exc}", file=sys.stderr)
        return 2

    if found is None:
        print(f"{date_to_digits(start)} 之后 {DEFAULT_MAX_DAYS} 天内没有回文日期")
        return 0
    print(f"{date_to_digits(start)} 之后第一个回文日期是 {date_to_digits(found)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
