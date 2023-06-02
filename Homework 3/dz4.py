class BaseClass1:
    def __init__(self):
        self.attribute1 = "Attribute 1"

    def method1(self):
        print("Method 1")


class BaseClass2:
    def __init__(self):
        self.attribute2 = "Attribute 2"

    def method2(self):
        print("Method 2")


class DerivedClass(BaseClass1, BaseClass2):
    def __init__(self):
        BaseClass1.__init__(self)
        BaseClass2.__init__(self)
        self.attribute3 = "Attribute 3"

    def method3(self):
        print("Method 3")

    def method1(self):
        BaseClass1.method1(self)
        print("Modified Method 1")


obj = DerivedClass()

print(obj.attribute1)
obj.method1()
obj.method2()

print(obj.attribute3)
obj.method3()