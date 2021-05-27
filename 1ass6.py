#!/usr/bin/env python
# coding: utf-8

# #1
# These are special characters used in representing whtespace characters.\ is used in escape characters.

# #2
# \n - Prints in new line
# \t - Creates horizontal tab space.

# #3
# Use of 2 backslashs can include escape characters.
# eg :"I'm Sherin \\Shaji

# In[ ]:


#4 
Since the text starts with double quotes the compiler considers whatever enclosed within it.So single quotes get printed.Vice versa is also possible.


# #5
# By default print() uses '\n' as delimeter.So without providing it automatically string gets printed in new line

# In[52]:


#6
x='Hello, world'[1]
y='Hello, world'[0:5]
z='Hello, world'[:5]
u='Hello, world'[3:]
l=[x,y,z,u]
print(l)


# In[53]:


#7
x='Hello'.upper()
y='Hello'.upper().isupper()
z='Hello'.upper().lower()
l=[x,y,z]
print(l)


# In[58]:


#8
x='Remember, remember, the fifth of July.'.split()
y='-'.join('There can only one.'.split())
print('x --',x)
print('y--',y)


# #9
# rjust() = The method alligns the string to the right and fills the remaining space with blank space or any other characters as specified in 'fillchr' argument.
# ljust() = The method alligns the string to the left and fills the remaining space with blank space or any other characters as specified in 'fillchr' argument.
# center() = Alligns the string according to width specified and fills the remaining with blank space

# In[ ]:


#10
string.trim() method removes whitespace characters from satrt and end and returns string with no white spaces
.trimstart()= removes from begining
.trimend()= removes from end

