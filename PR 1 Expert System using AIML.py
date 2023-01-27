#!/usr/bin/env python
# coding: utf-8

# In[10]:


info = []
name = input("Enter your name : ")
age = input("Enter your age : ")
info.append(name)
info.append(age)
print(info)

a=['fever','headache','vomiting']
b=['thirstyness','weightloss','blurryvision']
print(a,b)

symptoms = input("Enter Symptoms as seen above : ")
list = symptoms.split(",")
symptoms.lower()
print(info)


for i in list:
    print(i)
    
if i.strip() in a:
    print("You may have malaria")
    print("Please visit a doctor")
    if i.strip() in b:
        print("You may have Diabetes")
        print("Consume less sugar")
else:
    print("Symptoms do not match")


# In[ ]:





# In[ ]:




