#!/usr/bin/env python
# coding: utf-8

# In[36]:


import json
import datetime
fd=open("./record.json","r")
r=fd.read()
fd.close()
print("******")
print("Hi, Welcome to Robert Supermarket")
print("******")
print('These things are available ')
print("--------->")
print(r)


# In[37]:


#type(r)


# In[38]:


record=json.loads(r)
#print(record)


# ## add
# 

# In[39]:



prod_id = str(input("Enter product id:"))


#add here if item already exist
if prod_id in record.keys():
    pr = int(input("Enter price:"))                  #here we ask price, because price might be increase due to inflation 
    qn = int(input("Enter quantity:"))
    record[prod_id] = {'name': name, 'pr': pr, 'qn': qn+ record[prod_id]["qn"]}
#here if doesn't exist
else:
    name = str(input("Enter name:"))
    pr = int(input("Enter price:"))
    qn = int(input("Enter quantity:"))
    record[prod_id] = {'name': name, 'pr': pr, 'qn': qn}

js = json.dumps(record)

fd = open("record.json",'w')
fd.write(js)
fd.close()


# In[ ]:




