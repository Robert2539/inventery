#!/usr/bin/env python
# coding: utf-8

# In[78]:


import json

fd = open("record.json",'r')
r = fd.read()
fd.close()

records = json.loads(r)


# In[79]:



#records


# In[80]:


import random

ui_prod  = str(input("Enter the product_Id: "))
ui_quant = int(input("Enter the quantity: "))

if (ui_quant<records[ui_prod]['pr']):
    
    
    print("Product: ", records[ui_prod]['name'])
    print("Price: ", records[ui_prod]['pr'])
    print("Billing Amount: ", records[ui_prod]['pr'] * ui_quant)
    sales_id=sales_id+random.randint(1000000,100000000)
    print("sales is is :",sales_id)
    records[ui_prod]['qn'] = records[ui_prod]['qn'] - ui_quant
else:
    print("sorry, less items there than you are expecting")


# In[81]:


js = json.dumps(records)

fd = open("record.json",'w')
fd.write(js)
fd.close()


# In[82]:


sales = {sales_id : {'prod' : ui_prod, 'qn' : ui_quant, 'amount': records[ui_prod]['pr'] * ui_quant}}
sales[sales_id] = {'prod' : ui_prod, 'qn' : ui_quant, 'amount': records[ui_prod]['pr'] * ui_quant}


# In[83]:


ss=json.dumps(sales)
sl=open("sales.json",'a')
sl.write(ss)
sl.close()


# In[ ]:




