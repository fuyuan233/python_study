# Writer :fuyuan360
# Email  :fuyuan360@qq.com
class Car:
    def __init__(self,name,**keywords):
        self.name = name
        self.attrabutes = keywords
    def __getattr__(self, item):
            return self.attrabutes[item]

benz = Car( name="Benz",color="black",price=139499)
if benz.price > 100000:
    print(benz.name)