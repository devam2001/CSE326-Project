#!/usr/bin/env python
# coding: utf-8

# In[1]:


#List Elements
#a=[1,2,3] #homogenous
a=[1,"hi",2.3]
print(a)


# In[8]:


#important functions
my_list=[1,2,42,21,1,3,4]
#print(Len(my_list))
#print(my_List.index(3))
#print(my_List.count(21))
#my_list.sort()             #asc
my_list.sort(reverse=True) #desc
print(my_list)
my_list.reverse()
print(my_list)


# In[15]:


my_ist=[1,2,4]
#my_list.append(3)
my_list.extend([5,6])
print(my_list)


# In[16]:


my_list.insert(2,3)   #insert(index,element)
print(my_list)


# In[ ]:




