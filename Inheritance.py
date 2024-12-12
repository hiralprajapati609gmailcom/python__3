class A:
    def getA(self,a):
        self.a=a
    def putA(self):
        print("A : ",self.a)
class B(A):
    def getB(self,b):
        self.b=b
    def putB(self):
        print("B : ",self.b)
class C(B):
    def getC(self,c):
        self.c=c
    def putc(self):
        print("C : ",self.c)
class D(B,C):
    def get(self,d):
        self.d=d
    def putD(self):
        print("D : ",self.d)
d1=D()

d1.getA(10)
d1.getb(20)
d1.getc(30)
d1.getD(40)
d1.putA()
d1.putB()
d1.putC()
d1.putD()
