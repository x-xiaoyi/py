"""面向对象练习：学生模型、学生名册、继承与多态。"""

from .inheritance_demo import Device, Smartphone, Smartwatch, Tablet
from .student import Student
from .student_management import StudentManagement

__all__ = [
    "Device",
    "Smartphone",
    "Smartwatch",
    "Student",
    "StudentManagement",
    "Tablet",
]
