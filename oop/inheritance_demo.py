"""继承与多态练习（原 ``jicheng.py``，"jicheng" 就是"继承"的拼音）。

保留原来的教学意图：``Device`` 是父类，``Smartphone`` / ``Smartwatch`` / ``Tablet``
继承它，其中 ``Smartwatch`` 重写 ``power_on()`` 演示多态；``__brand`` 用双下划线做
私有属性，只能通过 ``brand`` 属性 / ``set_brand()`` 访问。

顺手修掉的问题：类名小写、``temprature`` 拼写、``pingmu`` 拼音、所有代码写在模块
顶层（import 即执行，没有 ``if __name__ == "__main__":`` 守卫）、被拒绝的品牌名
没有任何返回值。

用法::

    python oop/inheritance_demo.py
"""

from __future__ import annotations

INVALID_BRAND = "shanzai"  # 山寨


class Device:
    """电子设备基类。

    Attributes:
        brand: 品牌名（只读属性，改品牌请用 :meth:`set_brand`）。
    """

    def __init__(self, brand: str) -> None:
        """初始化设备。

        Args:
            brand: 品牌名。
        """
        self.__brand = brand

    @property
    def brand(self) -> str:
        """品牌名。"""
        return self.__brand

    def set_brand(self, new_brand: str) -> bool:
        """修改品牌名。

        Args:
            new_brand: 新品牌名。

        Returns:
            修改成功返回 True；``new_brand`` 是 "shanzai" 时拒绝修改并返回 False。

        修复: 旧代码被拒绝时只 print，不给返回值，调用方无法判断是否改成功。
        """
        if new_brand == INVALID_BRAND:
            print("invalid brand name")
            return False
        self.__brand = new_brand
        return True

    def power_on(self) -> None:
        """开机（子类可重写）。"""
        print("the device is on now")


class Smartphone(Device):
    """智能手机。"""

    def __init__(self, brand: str, screen_size: str) -> None:
        # 修复: 旧代码把屏幕尺寸写成 print(f"pingmu:{...}") 里的拼音，属性名统一成 screen_size。
        super().__init__(brand)
        self.screen_size = screen_size


class Smartwatch(Device):
    """智能手表，重写 ``power_on()`` 演示多态。"""

    def __init__(self, brand: str, temperature: str) -> None:
        # 修复: 旧代码属性名 temprature 拼写错误，已改为 temperature。
        super().__init__(brand)
        self.temperature = temperature

    def power_on(self) -> None:
        """开机（覆盖父类实现）。"""
        print("the smartwatch is on now")


class Tablet(Device):
    """平板电脑。"""

    def __init__(self, brand: str, weight: str) -> None:
        super().__init__(brand)
        self.weight = weight


def main() -> int:
    """构造三种设备，演示继承、属性封装与多态。"""
    my_phone = Smartphone("huawei", "6.7inch")
    my_watch = Smartwatch("xiaomi", "36.5C")
    my_tablet = Tablet("apple", "500g")

    print(f"brand:{my_phone.brand}")
    print(f"screen:{my_phone.screen_size}")
    print(f"temperature:{my_watch.temperature}")
    print(f"weight:{my_tablet.weight}")

    for device in (my_phone, my_watch, my_tablet):
        device.power_on()  # 多态：Smartwatch 走自己的 power_on

    # 父类 set_brand 的白名单校验在子类实例上同样生效
    print("改品牌成功?", my_phone.set_brand("honor"), "->", my_phone.brand)
    print("改品牌成功?", my_phone.set_brand(INVALID_BRAND), "->", my_phone.brand)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
