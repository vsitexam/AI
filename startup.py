#!/usr/bin/env python
# coding: utf-8

# In[1]:


import aiml


# In[2]:


kernel=aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")


# In[ ]:


while True:
    input_text=input("> Human : ")
    response = kernel.respond(input_text)
    print("> Bot : "+response)


# In[ ]:




