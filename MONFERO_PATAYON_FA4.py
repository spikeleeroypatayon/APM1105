#!/usr/bin/env python
# coding: utf-8

# Write a function named ack that evaluates the Ackermann function. Use your function to evaluate ack(2,4). What happens for larger values of m and n?

# In[8]:


def ack(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

    
print(ack(2,4))


# In[9]:


m=int(input("input value for m: "))
n=int(input("input value for n: "))

print(ack(m,n))


# for larger values of m and n, as per recursive, the larger the values of m and n the longer the process of evaluating of the value.
