
class Device:
    def __init__(self,brand):
        self.__brand=brand
    def power_on(self):
        print("the device is on now")
    def get_brand(self):
        return self.__brand
    def set_brand(self,new_brand):
        if new_brand=="shanzai":
            print("invalid brand name")
        else:
            self.__brand=new_brand
    
class smartphone(Device):
    def __init__(self,brand,screen_size):
        super().__init__(brand)
        self.screen_size=screen_size

my_phone=smartphone("huawei","6.7inch")
print(f"brand:{my_phone.get_brand()}")
print(f"pingmu:{my_phone.screen_size}")

class smartwatch(Device):
    def __init__(self,brand,temprature):
        super().__init__(brand)
        self.temprature=temprature
    def power_on(self):
        print("the smartwatch is on now")
my_watch=smartwatch("xiaomi","36.5C")
my_inventory=[my_phone,my_watch]

for i in my_inventory:
    i.power_on()
class tablet(Device):
    def __init__(self,brand,weight):
        super().__init__(brand)
        self.weight=weight
t=tablet("apple","500g")
p=smartphone("samsung","7inch")
my_phone.set_brand("shanzai")