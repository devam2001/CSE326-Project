#!/usr/bin/env python
# coding: utf-8

# In[10]:


# 2 or more base/parent/super ----multiple

class a:
        a1=0
class b:
        b1=0
class c(a,b):
        c1=0
    def read(self):
        self.a1=input("Enter the value of a1:")
        self.b1=input("Enter the value of b1:")
        self.c1=input("Enter the value of c1:")
    def display(self):
        print(type(self.a1))
        print(type(self.b1))
        print((self.c1))
obj=c()
obj.read()
obj.display()


# In[6]:


class a:
        a1=0
class b:
        b1=0
class c(a,b):
        c1=0
    def read(self):
        self.a1=int(input("Enter the value of a1:"))
        self.b1=int(input("Enter the value of b1:"))
        self.c1=int(input("Enter the value of c1:"))
    def display(self):
        print(self.a1)
        print(self.b1)
        print(self.c1)
obj=c()
obj.read()
obj.display()


# In[19]:


"""WAP in python to create two calsses box and child box having 3 diff. 
    data members calculate the area of box using the concept of single level inheritance """

class box:
       def __init__(self):
            length=0
            breadth=0
            height=0
class child_box(box):
    
    def area(self):
        self.length=int(input("Enter length of box "))
        self.breadth=int(input("Enter breadth of box "))
        self.height=int(input("Enter height of box "))
    def display(self):
        print(self.length* self.breadth*self.height)
obj=child_box()
obj.area()
obj.display()


# In[ ]:




