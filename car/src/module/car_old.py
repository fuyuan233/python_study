# Author fuyuan: fuyuan360@qq.com
class Car:
    def __init__(self, make, model, **kwargs):
        self.make = make
        self.model = model
        self.attributes = kwargs

    def __getattr__(self, arg):
        if arg in self.attributes:
            return self.attributes[arg]
        else:
            raise AttributeError(f"Car object has no attribute '{arg}'")


# 示例
ford = Car("Ford", "F150", color="red")
print(ford.color)
print(ford.aer)
