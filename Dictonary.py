#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Program for counting the occurence of the element

def demo(string):#pineapple
 d={}
 for char in string:
    if char not in d:
     d[char]=1
    else:
     d[char]=d[char]+1
    return d
print(demo("pineapple"))


# In[10]:


"""Write a program to print the count of positive and negative nos. When the list of numbers is passed to the function. 
The output should be in the form of dictionary."""
def demo(L):
 d={}
 d["pos"]=0
 d["neg"]=0
 for num in L:
    if num>0:
        d["pos"]+=1
    else:
        d["neg"]+=1
        print(d)
L=[1,-2,-3,4]
demo(L)


# In[ ]:


#write a program to compare two list and print the common elements along with the count of the common elements

