#!/usr/bin/env python
# coding: utf-8

# # Session 1
# 
# Assignment 1 Question
# 
# ​ Problem Statement
# 
# 1. Install Jupyter notebook and run the first program and share the screenshot of the output.
# LINK
# 
# 2. Write a program which will find all such numbers which are divisible by 7 but are not a
# multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
# in a comma-separated sequence on a single line.
# 
# 3. Write a Python program to accept the user's first and last name and then getting them printed
# in the the reverse order with a space between first name and last name.
# 
# 4. Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r**3
# 

# ## Output of problem statement 1
# 1. Install Jupyter notebook and run the first program and share the screenshot of the output.
# 
# 
# 
# <img src="Python_session1_image.png">

# ## Output of problem statement 2

# In[20]:


#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
#between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

l =[]
for val in range(2000, 3201):
       if val %7==0 and val %5 !=0:
              
            l.append(val)
print(l)


# ## Output of problem statement 3

# In[22]:


#3. Write a Python program to accept the user's first and last name and then getting them printed in the the 
#reverse order with a space between first name and last name.

first_name= input("Enter your First Name:")
last_name = input("Enter your Last Name :")
print(first_name[::-1], last_name[::-1])


# ## Output of problem statement 4

# In[25]:


#Write a Python program to find the volume of a sphere with diameter 12 cm. Formula: V=4/3 * π * r**3

def volume_sphere (diameter):
    volume = (4/3)* (22/7)*((diameter/2)**3)
    return volume
print("Volume of radius with diameter 12CM = %f:" %volume_sphere(12))


# In[ ]:




