#!/usr/bin/env python
# coding: utf-8

# In[9]:


#init Constructor

class box:
    width=0   # instance variable
    height=0
    depth=0
    volume=0
    def __init__(self):  #it is used to assign values to the instance variable
        self.width=5
        self.height=5
        self.depth=5
        print(self.width*self.height*self.depth)
    def vol(self):
        return self.width*self.height*self.depth
obj=box()
print(obj.width)
print("Volume=",obj.vol())


# In[10]:


#private data member

class demo:
    def __init__(self):
        self.name="Elon Musk"
        self.__accno=10101012   #add __ before name
    def display(self): 
        print("Name ",self.name)
        print("Account No. ",self.__accno)
obj=demo()
print("Name outside of the class ",obj.name)
#print("Account No. outside of the class ",obj.accno)
obj.display()


# In[ ]:


"""Write a program in python having class name student consisting of both 
public and private data members create a function which will display all 
the data members"""

class student:
    def __init__(self):
        self.name="Devam"
        self.regno="11908405"
        self.__cgpa=8
        self.__phone=1234567890
    def display(self):
        print("Name ",self.name)
        print("Registration No ",self.regno)
        print("CGPA ",self.__cgpa)
        print("Phone ",self.__phone)
obj=student()
print("Name: ")

