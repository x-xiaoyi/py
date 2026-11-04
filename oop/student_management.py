"""学生管理：增 / 查 / 删 / 列（原 ``studentManagement.py`` + ``leiceshi.py``）。

旧代码问题（逐条对应下面 ``# 修复:`` 注释）：

1. ``leiceshi.py`` 里 ``from leiceshi import student`` 是**自引用**，
   ``studentManagement.py`` 又 ``from leiceshi import student``，两边互为循环导入；
   而且 ``student`` 类其实定义在 ``le.py`` 里。
2. ``self.studentts`` 拼写多了一个 ``t``，删除时必 AttributeError。
3. 删除逻辑用了根本不存在的 ``self.student``，且删完不 break、未命中时对每个元素
   都打印一次"没找到"。
4. 原来的入口脚本 ``leiceshi.py`` 只有 6 行演示，已并入本文件的 ``demo()``。

用法::

    python oop/student_management.py
"""

from __future__ import annotations

try:  # 以包方式导入（pytest / python -m oop.student_management）
    from oop.student import Student
except ImportError:  # python oop/student_management.py 直跑时 sys.path[0] 是 oop/
    from student import Student


class StudentManagement:
    """一个内存版的学生名册。

    Attributes:
        students: 已登记的学生列表。

    Example:
        >>> book = StudentManagement()
        >>> book.add_student("fy", "18", "A").name
        'fy'
    """

    def __init__(self) -> None:
        """初始化空名册。"""
        # 修复: 旧代码写的是 self.studentts（多一个 t），任何后续访问都是 AttributeError。
        self.students: list[Student] = []

    def add_student(self, name: str, age: int | str, grad: str) -> Student:
        """登记一名学生并返回其对象。

        Raises:
            ValueError: 姓名/年龄非法。
        """
        new_student = Student(name, age, grad)
        self.students.append(new_student)
        print(f"学生:{new_student.name}添加成功")
        return new_student

    def find_student(self, name: str) -> Student | None:
        """按姓名查找，返回第一个匹配的学生；没有则返回 None。

        原名 ``found_student`` 是语法错误的英文，改为 ``find_student``。
        """
        for student in self.students:
            if student.name == name:
                return student
        return None

    def delete_student(self, name: str) -> bool:
        """按姓名删除第一名匹配的学生。

        Returns:
            删除成功返回 True，没有这个人返回 False。

        修复: 旧代码遍历不存在的 ``self.studentts``，且用 ``self.student.remove(b)``
        删除一个从未定义的属性；命中后不 break，未命中还会对每个元素打印一次"没找到"。
        """
        for index, student in enumerate(self.students):
            if student.name == name:
                del self.students[index]
                print("now,student has already been deleted")
                return True
        print("sorry, we not found, try again")
        return False

    def list_students(self) -> list[Student]:
        """返回名册中所有学生（副本，避免外部改动内部列表）。"""
        return list(self.students)


def demo() -> None:
    """原 ``leiceshi.py`` 的演示流程：加两个人、查一个不存在的人、再删一个人。"""
    manager = StudentManagement()
    manager.add_student("fy", "18", "A")
    manager.add_student("liu", "14", "B")

    if manager.find_student("yy") is None:
        print("sorry, we not found, try again")
    # 旧脚本只查了不存在的 'yy' 就结束了，这里补上命中、删除、再列出。
    if (found := manager.find_student("fy")) is not None:
        print("yes,we found it")
        found.display_info()
    manager.delete_student("liu")
    print("剩余学生:", manager.list_students())


def main() -> int:
    """运行演示。"""
    demo()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
