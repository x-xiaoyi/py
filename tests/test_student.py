"""``Student`` 数据模型的单元测试。"""

import pytest

from oop.student import Student


def test_age_string_is_coerced_to_int():
    """演示脚本里传的是 "18" 这种字符串，模型内部要统一成 int。"""
    student = Student("fy", "18", "A")
    assert student.age == 18
    assert isinstance(student.age, int)


def test_zero_age_is_allowed():
    assert Student("baby", 0, "A").age == 0


@pytest.mark.parametrize("age", [-1, -18])
def test_negative_age_is_rejected(age):
    with pytest.raises(ValueError, match="负数"):
        Student("fy", age, "A")


@pytest.mark.parametrize("age", ["abc", None, "1.5"])
def test_non_integer_age_is_rejected(age):
    with pytest.raises(ValueError, match="整数"):
        Student("fy", age, "A")


@pytest.mark.parametrize("name", ["", "   "])
def test_empty_name_is_rejected(name):
    with pytest.raises(ValueError, match="姓名"):
        Student(name, 18, "A")


def test_display_info_prints_three_lines(capsys):
    Student("fy", 18, "A").display_info()
    assert capsys.readouterr().out == "name: fy\nage: 18\ngrad: A\n"


def test_set_age_overwrites_and_prints(capsys):
    student = Student("fy", 18, "A")
    student.set_age("20")
    assert student.age == 20
    assert capsys.readouterr().out == "new age is: 20\n"


def test_set_age_rejects_negative():
    student = Student("fy", 18, "A")
    with pytest.raises(ValueError, match="负数"):
        student.set_age(-1)


def test_repr_is_readable():
    assert repr(Student("fy", 18, "A")) == "Student(name='fy', age=18, grad='A')"
