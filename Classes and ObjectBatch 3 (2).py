{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#Class\n",
    "--User defined Datatype\n",
    "--Blue Print of an Object\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sample\n",
      "<__main__.Demo object at 0x000002891D26E4A8>\n"
     ]
    }
   ],
   "source": [
    "class Demo:\n",
    "    print(\"Sample\")\n",
    "d=Demo()\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "this is my first program\n",
      "<__main__.program object at 0x000002891D26E5C0>\n"
     ]
    }
   ],
   "source": [
    "class program:\n",
    "    print(\"this is my first program\")\n",
    "p=program()\n",
    "print(p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "# Data Members \n",
    "\n",
    "class rectangle:\n",
    "    length=0\n",
    "    width=0\n",
    "r=rectangle()\n",
    "print(rectangle.length)#accessing the data members\n",
    "print(r.width)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the length20\n",
      "Enter the width30\n",
      "0\n",
      "20\n",
      "30\n"
     ]
    }
   ],
   "source": [
    "class rectangle:\n",
    "    length=0\n",
    "    width=0\n",
    "r=rectangle()\n",
    "r.length=int(input(\"Enter the length\"))\n",
    "r.width=int(input(\"Enter the width\"))\n",
    "print(rectangle.length)#accessing the data members\n",
    "print(r.length)\n",
    "print(r.width)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to OOP\n"
     ]
    }
   ],
   "source": [
    "# Member Function\n",
    "class method:\n",
    "    def display(self):\n",
    "        print(\"Welcome to OOP\")\n",
    "m=method()\n",
    "m.display()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "78.5"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Member fun with multiple parameters\n",
    "class circle:\n",
    "    def area(self,r):\n",
    "        return 3.14*r**2\n",
    "c=circle()\n",
    "c.area(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Area of rectangle 20\n"
     ]
    }
   ],
   "source": [
    "class rectangle:\n",
    "    def area(self,l,w):\n",
    "        return l*w\n",
    "rr=rectangle()\n",
    "print(\"Area of rectangle\",rr.area(5,4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "#significance self parameter\n",
    "\n",
    "class imp:#2\n",
    "    x=5 # x=5\n",
    "    def show(self,x): #4\n",
    "        x=30  #5 \n",
    "        print(x) #6\n",
    "obj=imp()   #1\n",
    "obj.show(50) #3 x=50\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "class imp:\n",
    "    x=5 #instance value\n",
    "    def show(self,x): \n",
    "        x=30  #local value\n",
    "        print(x) \n",
    "        print(self.x)\n",
    "        #print(imp.x)\n",
    "obj=imp()\n",
    "obj.show(50) \n",
    "#print(obj.x)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Exit\n",
      "M from Method 2\n",
      "M from Method 1\n"
     ]
    }
   ],
   "source": [
    "class demo:\n",
    "    def method1(self): #7\n",
    "        print(\"M from Method 1\") #8\n",
    "    def method2(self):# 4\n",
    "        print(\"M from Method 2\") #5\n",
    "        self.method1() # 6\n",
    "a=demo() #1\n",
    "print(\"Exit\") #2\n",
    "a.method2() #3\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name:ss\n",
      "ss\n",
      "Enter your age:20\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "class Demo:\n",
    "    name=\"\"\n",
    "    age=0\n",
    "    def read(self):\n",
    "        name=input(\"Enter your name:\")\n",
    "        print(name)\n",
    "        age=int(input(\"Enter your age:\"))\n",
    "        print(age)\n",
    "d1=Demo()\n",
    "d1.read()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#Summary\n",
    "class\n",
    "object\n",
    "data member\n",
    "member function\n",
    "self parameter\n",
    "dynamic input inside the class\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sagar\n",
      "Name is : sagar\n",
      "Account Details: 10100\n"
     ]
    }
   ],
   "source": [
    "#Private Data Members\n",
    "\n",
    "class person:\n",
    "    def __init__(self):\n",
    "        self.name=\"sagar\" #public\n",
    "        self.__bank= 10100  #private\n",
    "    def display(self):\n",
    "        print(\"Name is :\",self.name)\n",
    "        #print(\"Account Details:\",self.bank)\n",
    "        print(\"Account Details:\",self.__bank) # how to access the variable privately\n",
    "p=person()\n",
    "print(p.name)\n",
    "p.display()\n",
    "#print(p.__bank)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "78.5\n"
     ]
    }
   ],
   "source": [
    "# __init__ Method\n",
    "\n",
    "class circle:\n",
    "    pi=0        #data type identification\n",
    "    r=0\n",
    "    def __init__(self):\n",
    "        self.pi=3.14  # variable initialize\n",
    "        self.r=5\n",
    "    def area(self):\n",
    "        print(self.r)\n",
    "        return self.pi*self.r**2\n",
    "c=circle()\n",
    "print(c.area())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Test1= True\n",
      "Test2= False\n"
     ]
    }
   ],
   "source": [
    "#Passing object as an function argument\n",
    "class test:\n",
    "    a=0\n",
    "    b=0\n",
    "    def __init__(self,x,y): # x=10,y=20\n",
    "        self.a=x #10\n",
    "        self.b=y #20\n",
    "    def equal(self,obj): # 20,30\n",
    "        if (obj.a==self.a and obj.b==self.b):  # (10==10 and 30==20)---#incorrect\n",
    "            return True\n",
    "        else:\n",
    "            return False\n",
    "obj1=test(10,20)#obj1\n",
    "obj2=test(10,20)\n",
    "obj3=test(10,30)\n",
    "print(\"Test1=\",obj1.equal(obj2))   #obj1==>a=10,b=20.....................obj2==> a=10,b=20=====>>>TRUE\n",
    "print(\"Test2=\",obj1.equal(obj3))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome\n",
      "hello\n",
      "Destructor executed successfully\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'obj1' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-24-edd1c831a560>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[1;32mdel\u001b[0m \u001b[0mobj2\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m \u001b[1;32mdel\u001b[0m \u001b[0mobj3\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 14\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mid\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mobj1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m: name 'obj1' is not defined"
     ]
    }
   ],
   "source": [
    "# DESTRUCTOR\n",
    "class demo:\n",
    "    def __init__(self):\n",
    "        print(\"Welcome\")\n",
    "    def __del__(self):\n",
    "        print(\"Destructor executed successfully\")\n",
    "obj1=demo()#cons call\n",
    "obj2=obj1\n",
    "obj3=obj1\n",
    "print(\"hello\") # unique\n",
    "del obj1\n",
    "del obj2\n",
    "del obj3\n",
    "print(id(obj1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#class membership\n",
    "\n",
    "class a:\n",
    "    pass\n",
    "class b:\n",
    "    pass\n",
    "class c:\n",
    "    pass\n",
    "obj1=a()\n",
    "obj2=b()\n",
    "obj3=c()\n",
    "\n",
    "isinstance(obj1,a)\n",
    "isinstance(obj2,a)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "600\n"
     ]
    }
   ],
   "source": [
    "#Method Overloading\n",
    "class overload:\n",
    "    def add(self,a,b):\n",
    "        print(a+b)\n",
    "    def add(self,a,b,c):\n",
    "        print(a+b+c)\n",
    "o=overload()\n",
    "o.add(100,200,300)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100.2\n",
      "hi hello how are you \n"
     ]
    }
   ],
   "source": [
    "class demo:\n",
    "    result=0\n",
    "    def add(self,instanceof=None,*args):\n",
    "        if instanceof ==\"int\":\n",
    "            self.result=0\n",
    "        if instanceof ==\"str\":\n",
    "            self.result=\"\"\n",
    "        for i in args:\n",
    "            self.result=self.result+i\n",
    "        return self.result\n",
    "d=demo()\n",
    "print(d.add(\"int\",10.2,20,30,40))\n",
    "print(d.add(\"str\",\"hi \",\"hello \",\"how are you \"))\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Most Welcome\n",
      "Welcome Modiji\n"
     ]
    }
   ],
   "source": [
    "class over:\n",
    "    def greet(self,name=None): #4 name=Modiji\n",
    "        if name is not None:#8\n",
    "            print(\"Welcome \"+ name)#9\n",
    "        else:#5\n",
    "            print(\"Most Welcome\") #6\n",
    "obj=over()  #1\n",
    "obj.greet() #2\n",
    "obj.greet(\"Modiji\")#7\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Operator Overloading\n",
    "\n",
    "# x+y    __add__(self,other)\n",
    "# x-y     __sub__(self,other)\n",
    "# x*y     __mul__(self,other)\n",
    "# x/y     __truediv__(self,other)\n",
    "# x//y     __floordiv__(self,other)\n",
    "# x%y     __mod__(self,other)\n",
    "# -x     __neg__(self,other)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the value of obj1:  20\n",
      "the value of obj2:  30\n",
      "50\n"
     ]
    }
   ],
   "source": [
    "class operator:\n",
    "    def __init__(self,x):#20\n",
    "        self.x=x #self.x=20\n",
    "    def __add__(self,other):\n",
    "        print(\"the value of obj1: \",self.x)\n",
    "        print(\"the value of obj2: \",other.x)\n",
    "        return(self.x+other.x)\n",
    "obj1=operator(20)\n",
    "obj2=operator(30)\n",
    "\n",
    "obj3=obj1+obj2\n",
    "print(obj3)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Special Method for comparing \n",
    "\n",
    "# x==y  __eq__(self,other)\n",
    "# x<y   __lt__(self,other)\n",
    "# x>y   __gt(self,other)\n",
    "# x<=y  __le__(self,other)\n",
    "# x>=y  __ge__(self,other)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The value of obj1= 20\n",
      "The value of obj2= 30\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "class demo:\n",
    "    def __init__(self,x):\n",
    "        self.x=x\n",
    "    def __lt__(self,other):\n",
    "        print(\"The value of obj1=\",self.x)\n",
    "        print(\"The value of obj2=\",other.x)\n",
    "        return(self.x<other.x)\n",
    "obj1=demo(20)\n",
    "obj2=demo(30)\n",
    "print(obj1<obj2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Inheritance single,multilevel,multiple,heri,hyr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "m from class a\n",
      "m from class b\n"
     ]
    }
   ],
   "source": [
    "#single Inheritance\n",
    "\n",
    "class a:\n",
    "    print(\"m from class a\")\n",
    "class b(a):\n",
    "    print(\"m from class b\")\n",
    "obj=a()\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "class parent:\n",
    "    def set(self,x,y):\n",
    "        self.x=x\n",
    "        self.y=y\n",
    "class child(parent): #single inh\n",
    "    def draw(self):\n",
    "        print(self.x)\n",
    "        print(self.y)\n",
    "\n",
    "c=child()\n",
    "c.set(10,20)\n",
    "c.draw()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "content of obj 1:\n",
      "100 200\n",
      "content of obj 2:\n",
      "300 400 500\n",
      "sum of all 3 elements is:\n",
      "1200\n"
     ]
    }
   ],
   "source": [
    "class a:\n",
    "    i=0\n",
    "    j=0\n",
    "    def showij(self):\n",
    "        print(self.i,self.j)\n",
    "class b:\n",
    "    k=0\n",
    "    def showijk(self):\n",
    "        print(self.i,self.j,self.k)\n",
    "    def sum(self):\n",
    "        print(self.i+self.j+self.k)\n",
    "obj1=a()\n",
    "obj2=b()\n",
    "obj1.i=100\n",
    "obj1.j=200\n",
    "print(\"content of obj 1:\")\n",
    "obj1.showij()\n",
    "obj2.i=300\n",
    "obj2.j=400\n",
    "obj2.k=500\n",
    "print(\"content of obj 2:\")\n",
    "obj2.showijk()\n",
    "print(\"sum of all 3 elements is:\")\n",
    "obj2.sum()\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#multilevel \n",
    "a--base\n",
    "|\n",
    "b--intermediate derived class\n",
    "|\n",
    "c--child \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Following values:\n",
      "Enter your name:ss\n",
      "Enter your age:20\n",
      "Enter your height:50\n",
      "Enter your weight:30\n",
      "ss 20 50 30\n"
     ]
    }
   ],
   "source": [
    "class a:            #base \n",
    "    name=\"\"\n",
    "    age=0\n",
    "class b(a):         #intermediate\n",
    "    height=\"\"\n",
    "class c(b):         #child\n",
    "    weight=\"\"\n",
    "    def read(self):\n",
    "        print(\"Enter the Following values:\")\n",
    "        self.name=input(\"Enter your name:\")\n",
    "        self.age=int(input(\"Enter your age:\"))\n",
    "        self.height=input(\"Enter your height:\")\n",
    "        self.weight=input(\"Enter your weight:\")\n",
    "    def display(self):\n",
    "        print(self.name, self.age, self.height,self.weight)\n",
    "        #print(\"Age:\",self.age)\n",
    "        #print(\"Height:\",self.height)\n",
    "        #print(\"Weight:\",self.weight)\n",
    "obj=c()\n",
    "obj.read()\n",
    "obj.display()\n",
    "\n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Following values:\n",
      "Enter your name:ss\n",
      "Enter your age:20\n",
      "Enter your height:33\n",
      "Enter your weight:32\n",
      "ss 20 33 32\n"
     ]
    }
   ],
   "source": [
    "# multiple\n",
    "\n",
    "class a:            #base 1\n",
    "    name=\"\"\n",
    "    age=0\n",
    "class b:         # base 2\n",
    "    height=\"\"\n",
    "class c(a,b):         #child-->a&b\n",
    "    weight=\"\"\n",
    "    def read(self):\n",
    "        print(\"Enter the Following values:\")\n",
    "        self.name=input(\"Enter your name:\")\n",
    "        self.age=int(input(\"Enter your age:\"))\n",
    "        self.height=input(\"Enter your height:\")\n",
    "        self.weight=input(\"Enter your weight:\")\n",
    "    def display(self):\n",
    "        print(self.name, self.age, self.height,self.weight)\n",
    "        #print(\"Age:\",self.age)\n",
    "        #print(\"Height:\",self.height)\n",
    "        #print(\"Weight:\",self.weight)\n",
    "obj=c()\n",
    "obj.read()\n",
    "obj.display()\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "       A\n",
    "    \n",
    "    |      |\n",
    "    B      C\n",
    "    |  --- |\n",
    "        |\n",
    "        D"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "M from child class\n",
      "M from base class\n"
     ]
    }
   ],
   "source": [
    "#Method Overriding\n",
    "\n",
    "class a:\n",
    "    i=0\n",
    "    def display(self):\n",
    "        print(\"M from base class\")\n",
    "class b(a):\n",
    "    i=0\n",
    "    def display(self):\n",
    "        print(\"M from child class\")\n",
    "        super().display()\n",
    "obj=b()\n",
    "obj.display()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100 200 300\n",
      "10 20 30 40\n"
     ]
    }
   ],
   "source": [
    "# Super Keyword\n",
    "class demo:\n",
    "    a=0\n",
    "    b=0\n",
    "    c=0\n",
    "    def __init__(self,a1,b1,c1):\n",
    "        self.a=a1\n",
    "        self.b=b1\n",
    "        self.c=c1\n",
    "    def display(self):\n",
    "        print(self.a,self.b,self.c)\n",
    "class new(demo):\n",
    "    d=0\n",
    "    def __init__(self,a1,b1,c1,d1):\n",
    "        self.d=d1\n",
    "        super().__init__(a1,b1,c1)\n",
    "    def display(self):\n",
    "        print(self.a,self.b,self.c,self.d)\n",
    "\n",
    "obj1=demo(100,200,300)\n",
    "obj1.display()\n",
    "obj2=new(10,20,30,40)\n",
    "obj2.display()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Class \n",
    "Object\n",
    "Attributes\n",
    "Method\n",
    "Constructor\n",
    "Destructor\n",
    "Method Overloading\n",
    "Method Overriding\n",
    "Operator Overloading\n",
    "Interitance\n",
    "Polymorphism\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
