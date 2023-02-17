#!/usr/bin/env python
# coding: utf-8

# 1. Write a Python function to multiply all the numbers in a list.
# 
# Sample List : (5, 6, -1, 2, 4, -2, -10, 7)

# In[1]:


def multiply_list(y):
    
    product = 1
    
    for x in y:
        product = product * x
    return product


# In[2]:


list1 = [5, 6, -1, 2, 4, -2, -10, 7]
print(multiply_list(list1))


# 2. Write a function that draws a grid

# In[49]:


def grid(row, col):
    for i in range(row):
        
        print("+" + "---+" * col)
        
        print("|" + "   |" * col)
        
        print("|" + "   |" * col)

        print("+" + "---+" * col)


# In[50]:


grid(4,4)


# In[ ]:




