#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Single Inheritance 
class a:
    print("Hello!! I'm From Base Class")
class b(a):
    print("Hello!! I'm From Derived Class")
obj=a()
    


# In[3]:


class parent:
    def set(self,x,y):
        self.x=x
        self.y=y
class child(parent):
    def draw(self):
        print("The value of x is ",self.x)
        print("The value of y is ",self.y)
obj=child()
obj.set(10,20)
obj.draw()


# In[20]:


class a:
    i=0
    j=0
    def showij(self):
        print(self.i,self.j,end=" ")  #100 200
class b(a):
    k=0
    def showijk(self):
        print(self.i,self.j,self.k,end=" ")  #10 20 30
    def sum(self):
        print(self.i+self.j+self.k,end=" ") #60
o1=a()
o2=b()
o1.i=100
o1.j=200
o1.showij()
o2.i=10
o2.j=20
o2.k=30
o2.showijk()
o2.sum()


# In[39]:


# Create a method in child class to display all the content.
class sample:
        name =" "
        age = 0
class a(sample):
        marks=" "
class b(a):
        height=" "
    def read(self):
        print("Enter details;")
        self.name=input("enter name")
        self.age=int(input("enter age"))
        self.marks=int(input("enter marks"))
        self.height=int(input("enter height"))
    def display(self):
        print("values are:")
        print("name is",self.name)
        print("age is",self.age)
        print("marks are",self.marks)
        print("height is",self.height)
obj=b()
obj.read()
obj.display()


# In[ ]:




