"""学生数据模型（原 ``le.py`` 里的 ``student`` 类）。

改动：

* 类名 ``student`` -> ``Student``（PEP 8：类用大驼峰）；
* 方法 ``display_inf0`` -> ``display_info``（原来的末尾是数字 0，是拼写错误）；
* 方法 ``upgrade_age(d)`` -> ``set_age(d)``（原名听起来像"涨一岁"，实际是直接覆盖）；
* 增加年龄校验、``__repr__``，方便打印和测试断言。

``student_management.py`` 与本模块被 ``leiceshi.py`` 以"互相 import"的方式绕成了
循环导入（``leiceshi`` -> ``studentManagement`` -> ``leiceshi``），现在依赖关系是单向的：
``student_management`` -> ``student``。
"""

from __future__ import annotations

from typing import Any


def _coerce_age(age: Any) -> int:
    """把年龄统一成非负整数。

    Raises:
        ValueError: 无法转成整数或为负数。
    """
    # 修复: 旧代码直接 self.age = b，演示里传的是字符串 "18"，后续做算术会 TypeError。
    try:
        value = int(age)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"年龄必须是整数，收到 {age!r}") from exc
    if value < 0:
        raise ValueError(f"年龄不能为负数，收到 {value}")
    return value


class Student:
    """一名学生：姓名、年龄、成绩等级。

    Attributes:
        name: 姓名。
        age: 年龄（非负整数）。
        grad: 成绩等级，如 ``"A"``。

    Example:
        >>> Student("fy", "18", "A").age
        18
    """

    def __init__(self, name: str, age: int | str, grad: str) -> None:
        """初始化学生。

        Args:
            name: 姓名，不能为空。
            age: 年龄，可传 int 或纯数字字符串。
            grad: 成绩等级。

        Raises:
            ValueError: 姓名为空或年龄非法。
        """
        if not str(name).strip():
            raise ValueError("姓名不能为空")
        self.name = str(name)
        self.age = _coerce_age(age)
        self.grad = grad

    def display_info(self) -> None:
        """打印学生信息（保持旧脚本的三行输出样式）。"""
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"grad: {self.grad}")

    def set_age(self, new_age: int | str) -> None:
        """把年龄改成 ``new_age``（覆盖，不是自增）。

        Raises:
            ValueError: 年龄非法。
        """
        self.age = _coerce_age(new_age)
        print(f"new age is: {self.age}")

    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, age={self.age!r}, grad={self.grad!r})"


__all__ = ["Student"]
