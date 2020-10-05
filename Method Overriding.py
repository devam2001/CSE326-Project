"""create a program in python consisting of three classes
and implement the concept of multiple inheritance.Assume
suitable data members and member function."""

class a:
    def p1(self):
    print("Base class A")
class b(a):
    def p1(self):
    print("Base Class B")
    a.p1(self)
class c(a):
    def p1(self):
    print("Base class C")
    a.p1(self)

ob1=b()
ob2=c()
ob1.p1()
ob2.p1()