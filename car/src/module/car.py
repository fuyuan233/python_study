# Author fuyuan: fuyuan360@qq.com
class Car:
    def __init__(self, make, model, **kwargs):
        self.make = make
        self.model = model
        self.__dict__.update(kwargs)


# 示例
ford = Car("Ford", "F150", color="red")
print(ford.color)
print(ford.aer)
