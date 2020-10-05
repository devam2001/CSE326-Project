#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#operator Overloading

#x+y __add__(self,others arg)
#x-y __sub__(self,other arg)
#x*y __mul__(self,other arg)
#x/y __trudiv(self,other)
#x//y __floordiv__(self,other)
#x%y __mod__(self,other)
#-x __neg__(self,other)


# In[2]:


class over:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        print("The val of o1 ",self.x)
        print("The val of o2 ",other.x)
        return(self.x+other.x)
o1=over(10)
o2=over(20)
o3=o1+o2
print(o3)


# In[14]:


class calculator:
    def __init__(self,x):
        self.x=x
        
    def __add__(self,a):
        print("The val of 1st var is ",self.x)
        print("The val of 2nd var is ",a.x)
        return (self.x+a.x)
    
    def __sub__(self,s):
        return (self.x-s.x)
    
    def __mul__(self,m):
        return (self.x*m.x)
    
    def __truediv__(self,d):
        return (self.x/d.x)
    def __floordiv__(self,df):
        return (self.x//df.x)
    
    def __mod__(self,mod):
        return (self.x%mod.x)
    
o1=calculator(int(input("Enter 1st var ")))
o2=calculator(int(input("Enter 2nd var ")))
o3=o1+o2,o1-o2,o1*o2,o1/o2,o1//o2,o1%o2
print("Addition: ",o3,"\nSubtraction: ",o3,"\nMultiplicaton: ",o3,"\nDevision: ",o3,"\nModulus: ",o3,"\nFloat Devision: ",o3)


# In[ ]:


#Special Method for comparison

#x==y __eq__ (self,other)
#x<y __lt__ (self,other)
#x>y __gt__ (self,other)
#x<=y __le__ (self,other)
#x>=y __ge__(self,other)


# In[15]:


class demo:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        print("The val of 1st var  ",self.x)
        print("The val of 2nd var  ",other.x)
        return self.x<other.x
    def __eq__(self,other):
        return self.x==other.x
    def __gt__(self,other):
        return self.x>other.x
    def __le__(self,other):
        return self.x<=other.x
    def __ge__(self,other):
        return self.x>=other.x
    
o1=demo(10)
o2=demo(20)
print("x<y ",o1<o2,"\nx==y ",o1==o2,"\nx>y ",o1>o2,"\nx<=y ",o1<=o2,"\nx>=y ",o1>=o2)


# In[ ]:




