#!/usr/bin/env python
# coding: utf-8

# #Class
# --User defined Datatype
# --Blue Print of an Object
# 

# In[1]:


class Demo:
    print("Sample")
d=Demo()
print(d)


# In[2]:


class program:
    print("this is my first program")
p=program()
print(p)


# In[3]:


# Data Members 

class rectangle:
    length=0
    width=0
r=rectangle()
print(rectangle.length)#accessing the data members
print(r.width)


# In[5]:


class rectangle:
    length=0
    width=0
r=rectangle()
r.length=int(input("Enter the length"))
r.width=int(input("Enter the width"))
print(rectangle.length)#accessing the data members
print(r.length)
print(r.width)


# In[6]:


# Member Function
class method:
    def display(self):
        print("Welcome to OOP")
m=method()
m.display()


# In[8]:


# Member fun with multiple parameters
class circle:
    def area(self,r):
        return 3.14*r**2
c=circle()
c.area(5)


# In[9]:


class rectangle:
    def area(self,l,w):
        return l*w
rr=rectangle()
print("Area of rectangle",rr.area(5,4))


# In[11]:


#significance self parameter

class imp:#2
    x=5 # x=5
    def show(self,x): #4
        x=30  #5 
        print(x) #6
obj=imp()   #1
obj.show(50) #3 x=50
        


# In[15]:


class imp:
    x=5 #instance value
    def show(self,x): 
        x=30  #local value
        print(x) 
        print(self.x)
        #print(imp.x)
obj=imp()
obj.show(50) 
#print(obj.x)


# In[18]:


class demo:
    def method1(self): #7
        print("M from Method 1") #8
    def method2(self):# 4
        print("M from Method 2") #5
        self.method1() # 6
a=demo() #1
print("Exit") #2
a.method2() #3
        


# In[22]:


class Demo:
    name=""
    age=0
    def read(self):
        name=input("Enter your name:")
        print(name)
        age=int(input("Enter your age:"))
        print(age)
d1=Demo()
d1.read()


# #Summary
# class
# object
# data member
# member function
# self parameter
# dynamic input inside the class
# 

# In[9]:


#Private Data Members

class person:
    def __init__(self):
        self.name="sagar" #public
        self.__bank= 10100  #private
    def display(self):
        print("Name is :",self.name)
        #print("Account Details:",self.bank)
        print("Account Details:",self.__bank) # how to access the variable privately
p=person()
print(p.name)
p.display()
#print(p.__bank)


# In[10]:


# __init__ Method

class circle:
    pi=0        #data type identification
    r=0
    def __init__(self):
        self.pi=3.14  # variable initialize
        self.r=5
    def area(self):
        print(self.r)
        return self.pi*self.r**2
c=circle()
print(c.area())


# In[16]:


#Passing object as an function argument
class test:
    a=0
    b=0
    def __init__(self,x,y): # x=10,y=20
        self.a=x #10
        self.b=y #20
    def equal(self,obj): # 20,30
        if (obj.a==self.a and obj.b==self.b):  # (10==10 and 30==20)---#incorrect
            return True
        else:
            return False
obj1=test(10,20)#obj1
obj2=test(10,20)
obj3=test(10,30)
print("Test1=",obj1.equal(obj2))   #obj1==>a=10,b=20.....................obj2==> a=10,b=20=====>>>TRUE
print("Test2=",obj1.equal(obj3))


# In[24]:


# DESTRUCTOR
class demo:
    def __init__(self):
        print("Welcome")
    def __del__(self):
        print("Destructor executed successfully")
obj1=demo()#cons call
obj2=obj1
obj3=obj1
print("hello") # unique
del obj1
del obj2
del obj3
print(id(obj1))


# In[26]:


#class membership

class a:
    pass
class b:
    pass
class c:
    pass
obj1=a()
obj2=b()
obj3=c()

isinstance(obj1,a)
isinstance(obj2,a)


# In[2]:


#Method Overloading
class overload:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
o=overload()
o.add(100,200,300)


# In[6]:


class demo:
    result=0
    def add(self,instanceof=None,*args):
        if instanceof =="int":
            self.result=0
        if instanceof =="str":
            self.result=""
        for i in args:
            self.result=self.result+i
        return self.result
d=demo()
print(d.add("int",10.2,20,30,40))
print(d.add("str","hi ","hello ","how are you "))
            


# In[7]:


class over:
    def greet(self,name=None): #4 name=Modiji
        if name is not None:#8
            print("Welcome "+ name)#9
        else:#5
            print("Most Welcome") #6
obj=over()  #1
obj.greet() #2
obj.greet("Modiji")#7


# In[ ]:


#Operator Overloading

# x+y    __add__(self,other)
# x-y     __sub__(self,other)
# x*y     __mul__(self,other)
# x/y     __truediv__(self,other)
# x//y     __floordiv__(self,other)
# x%y     __mod__(self,other)
# -x     __neg__(self,other)


# In[10]:


class operator:
    def __init__(self,x):#20
        self.x=x #self.x=20
    def __add__(self,other):
        print("the value of obj1: ",self.x)
        print("the value of obj2: ",other.x)
        return(self.x+other.x)
obj1=operator(20)
obj2=operator(30)

obj3=obj1+obj2
print(obj3)
        


# In[11]:


# Special Method for comparing 

# x==y  __eq__(self,other)
# x<y   __lt__(self,other)
# x>y   __gt(self,other)
# x<=y  __le__(self,other)
# x>=y  __ge__(self,other)


# In[12]:


class demo:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        print("The value of obj1=",self.x)
        print("The value of obj2=",other.x)
        return(self.x<other.x)
obj1=demo(20)
obj2=demo(30)
print(obj1<obj2)


# In[ ]:


#Inheritance single,multilevel,multiple,heri,hyr


# In[3]:


#single Inheritance

class a:
    print("m from class a")
class b(a):
    print("m from class b")
obj=a()
    


# In[4]:


class parent:
    def set(self,x,y):
        self.x=x
        self.y=y
class child(parent): #single inh
    def draw(self):
        print(self.x)
        print(self.y)

c=child()
c.set(10,20)
c.draw()


# In[8]:


class a:
    i=0
    j=0
    def showij(self):
        print(self.i,self.j)
class b:
    k=0
    def showijk(self):
        print(self.i,self.j,self.k)
    def sum(self):
        print(self.i+self.j+self.k)
obj1=a()
obj2=b()
obj1.i=100
obj1.j=200
print("content of obj 1:")
obj1.showij()
obj2.i=300
obj2.j=400
obj2.k=500
print("content of obj 2:")
obj2.showijk()
print("sum of all 3 elements is:")
obj2.sum()


# #multilevel 
# a--base
# |
# b--intermediate derived class
# |
# c--child 
# 
# 

# In[4]:


class a:            #base 
    name=""
    age=0
class b(a):         #intermediate
    height=""
class c(b):         #child
    weight=""
    def read(self):
        print("Enter the Following values:")
        self.name=input("Enter your name:")
        self.age=int(input("Enter your age:"))
        self.height=input("Enter your height:")
        self.weight=input("Enter your weight:")
    def display(self):
        print(self.name, self.age, self.height,self.weight)
        #print("Age:",self.age)
        #print("Height:",self.height)
        #print("Weight:",self.weight)
obj=c()
obj.read()
obj.display()

    
    
    
    
    
    


# In[5]:


# multiple

class a:            #base 1
    name=""
    age=0
class b:         # base 2
    height=""
class c(a,b):         #child-->a&b
    weight=""
    def read(self):
        print("Enter the Following values:")
        self.name=input("Enter your name:")
        self.age=int(input("Enter your age:"))
        self.height=input("Enter your height:")
        self.weight=input("Enter your weight:")
    def display(self):
        print(self.name, self.age, self.height,self.weight)
        #print("Age:",self.age)
        #print("Height:",self.height)
        #print("Weight:",self.weight)
obj=c()
obj.read()
obj.display()

    


#        A
#     
#     |      |
#     B      C
#     |  --- |
#         |
#         D

# In[7]:


#Method Overriding

class a:
    i=0
    def display(self):
        print("M from base class")
class b(a):
    i=0
    def display(self):
        print("M from child class")
        super().display()
obj=b()
obj.display()



# In[13]:


# Super Keyword
class demo:
    a=0
    b=0
    c=0
    def __init__(self,a1,b1,c1):
        self.a=a1
        self.b=b1
        self.c=c1
    def display(self):
        print(self.a,self.b,self.c)
class new(demo):
    d=0
    def __init__(self,a1,b1,c1,d1):
        self.d=d1
        super().__init__(a1,b1,c1)
    def display(self):
        print(self.a,self.b,self.c,self.d)

obj1=demo(100,200,300)
obj1.display()
obj2=new(10,20,30,40)
obj2.display()


# In[ ]:


Class 
Object
Attributes
Method
Constructor
Destructor
Method Overloading
Method Overriding
Operator Overloading
Interitance
Polymorphism

