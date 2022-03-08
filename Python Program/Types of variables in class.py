class Test:
    j=0
    def __init__(self,x):
        self.i=x    ##Instance Variable
        Test.j+=1   ##class Variable
    def show(self):
        print(self.i,Test.j)
t1=Test(10)
t2=Test(20)
t3=Test(30)
t1.show()
t2.show()
t3.show()
