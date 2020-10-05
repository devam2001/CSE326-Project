#!/usr/bin/env python
# coding: utf-8

# In[5]:


fruit="apple"
#print(fruit[1])
#print(len(fruit))


# In[11]:


#Last element
#print(fruit[-1])
#print(fruit[4])
length=len(fruit)
last=fruit[length-1]
print(last)


# In[23]:


#fruit1="grapes"

print("Enter Your Fav. Fruit: ")
fruit1=input()
index=0
while index<len(fruit1):
    char=fruit1[index]
    print(char)
    index+=1


# In[18]:


fruit2="apple"
for char in fruit2:  #char=char+1  fruit2=apple
    print(char)     #a p p l e


# In[36]:


fav="pineapple"
#print(fav[4:9])   #slicing
#print(fav[0:4])
#print(fav[:4])
#print(fav[::])
print(fav[::2])


# In[39]:


#String Inbuilt Functions


# In[57]:


color="orange, green, blue"
#print(len(color))
#print(color.find("a"))
#print(ascii_lowercase)
#print(ascii_uppercase)
#print(digits)
#print(color.isupper())
#print(color.islower())
#print(color.capitalize())
#print(color.title())
#print(color.lower())
#print(color.upper())
#print(color.isspace())
#print(color.isdigit())
#print(color.isalpha())
print(color.isalnum())


# In[70]:


#Recursion
def fact(n):  #3 n=5 4 3 2 1
    if n==1 or n==0:#6
        return 1#7
    else:  #4
        return(n*fact(n-1))#5 n=5*4*3*2*1
num=5 #1
print("Factorial",fact(num)) #2


# In[72]:


#printing A
pattern=""
for row in range(0,7):
    for column in range(0,7):
        if(((column==1 or column==5)and row!=0)or((row==0 or row==3)and(column>1 and column<5))):
            pattern=pattern+"a"
        else:
                pattern=" "
                pattern=pattern+"\n"
                print(pattern)
    




