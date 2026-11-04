"""继承与多态演示的单元测试。"""

import pytest

from oop.inheritance_demo import Device, Smartphone, Smartwatch, Tablet


def test_device_brand_property():
    assert Device("huawei").brand == "huawei"


def test_set_brand_updates_value():
    device = Device("huawei")
    assert device.set_brand("honor") is True
    assert device.brand == "honor"


def test_set_brand_rejects_shanzai(capsys):
    device = Device("huawei")
    assert device.set_brand("shanzai") is False
    assert device.brand == "huawei"
    assert "invalid brand name" in capsys.readouterr().out


def test_smartphone_inherits_brand_and_keeps_screen_size():
    phone = Smartphone("samsung", "7inch")
    assert (phone.brand, phone.screen_size) == ("samsung", "7inch")


def test_tablet_keeps_weight():
    assert Tablet("apple", "500g").weight == "500g"


def test_smartwatch_overrides_power_on(capsys):
    Smartwatch("xiaomi", "36.5C").power_on()
    assert capsys.readouterr().out == "the smartwatch is on now\n"


def test_device_power_on_default_message(capsys):
    Device("huawei").power_on()
    assert capsys.readouterr().out == "the device is on now\n"


def test_private_brand_is_not_directly_accessible():
    """双下划线属性被名字改写，外部拿不到 ``__brand``。"""
    device = Device("huawei")
    with pytest.raises(AttributeError):
        _ = device.__brand  # noqa: SLF001 - 故意断言私有属性不可直接访问
