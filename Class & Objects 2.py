#!/usr/bin/env python
# coding: utf-8

# In[2]:


class demo:
    def __init__(self):
        print("Welcome")
    def __del__(self):
        print("Destructure Executed")
obj1=demo()
obj2=demo()
obj3=demo()

del obj1
del obj2
del obj3


# In[10]:


# Method Overloading - same name and diff no. of arg
"""class overload:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
obj=overload()
obj.add(10,20)
obj.add(10,20,30)"""
class overload:
    def greet(self,name=None):
        if name is not None:
            print("Welcome "+name)
        else:
            print("Welcome")
obj=overload()
obj.greet()
obj.greet("Modiji")


# In[17]:


class demo:
    result=0
    def add(self,instanceof=None,*name):
        if instanceof=="int":
            self.result=0
        if instanceof=="str":
            self.result=""
        for i in sample:
            self.result+=i
        return self.result
obj=demo()
print(obj.add("int",10,20,30,40,987,4))
print(obj.add("str","i","love","python"))


# In[ ]:


"""Create a program in python having class name as geometry.
Calculate the area of square and rectangle assuming suitable data 
members and signifying the concept of method overloading"""

class geometry:
    def area(self,area=None,)

