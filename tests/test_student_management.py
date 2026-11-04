"""``StudentManagement`` 增删查改的单元测试。"""

import pytest

from oop.student import Student
from oop.student_management import StudentManagement, demo


@pytest.fixture
def book():
    """一个装好两名学生的空名册。"""
    manager = StudentManagement()
    manager.add_student("fy", "18", "A")
    manager.add_student("liu", "14", "B")
    return manager


def test_new_book_is_empty():
    assert StudentManagement().list_students() == []


def test_add_student_returns_student_and_appends(book):
    added = book.add_student("wang", 20, "C")
    assert isinstance(added, Student)
    assert [s.name for s in book.list_students()] == ["fy", "liu", "wang"]


def test_find_existing_student(book):
    assert book.find_student("liu").age == 14


def test_find_missing_student_returns_none(book):
    assert book.find_student("yy") is None


def test_delete_existing_student(book, capsys):
    assert book.delete_student("fy") is True
    assert [s.name for s in book.list_students()] == ["liu"]
    assert "deleted" in capsys.readouterr().out


def test_delete_missing_student_returns_false(book, capsys):
    """旧实现在这里会 AttributeError（self.studentts 不存在）。"""
    assert book.delete_student("yy") is False
    assert len(book.list_students()) == 2
    assert capsys.readouterr().out.count("not found") == 1


def test_delete_removes_only_first_duplicate(book):
    book.add_student("fy", "30", "A")
    assert book.delete_student("fy") is True
    assert [s.name for s in book.list_students()] == ["liu", "fy"]


def test_list_students_returns_copy(book):
    """外部改动返回的列表不应该影响名册内部状态。"""
    book.list_students().clear()
    assert len(book.list_students()) == 2


def test_add_student_rejects_bad_age(book):
    with pytest.raises(ValueError):
        book.add_student("bad", -1, "F")


def test_demo_runs_end_to_end(capsys):
    """原 leiceshi.py 的流程（加上循环导入修复后）能跑通。"""
    demo()
    out = capsys.readouterr().out
    assert "学生:fy添加成功" in out
    assert "yes,we found it" in out
    assert "now,student has already been deleted" in out
