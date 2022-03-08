########### Instance Method #####################
class Test:
    clsmsg="This is class variable"
    def __init__(self):
        self.msg="This is instance variable"
    def show(self):
        print(self.msg)
        self.msg="Hello"
        print(self.msg)
        print(self.__class__.clsmsg)
        self.__class__.clsmsg="Democlass"
        print(self.__class__.clsmsg)
t1=Test()
t1.show()
print("==============================================")

############ Class Method ######################
class Test:
    clsmsg="This is class variable"
    @classmethod
    def show(cls):
        print(cls.clsmsg)
        cls.clsmsg="Hello World"
        print(cls.clsmsg)
Test.show()
print("==============================================")

############ Static Variables ######################
class Test:
    @staticmethod
    def show():
        print("This is static variable")
Test.show()

