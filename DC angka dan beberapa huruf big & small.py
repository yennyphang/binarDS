#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


get_ipython().system('pip install numpy')


# In[3]:


import numpy as np
np.array(['a','b','c','d','e'],ndmin=2)


# In[4]:


a=np.array(['a','b',2,'3.0'])
a


# In[7]:


import pandas as pd
data={'Element':['Silver','Gold','Platinum','Copper'],'Atomic Number':[47,79,78,29]}
frame=pd.DataFrame(data,index=['element 1','element 2','element 3','element 4'])
frame


# In[8]:


frame.iloc[0:3,:]


# In[9]:


frame.rank()


# In[6]:


import re

text = "hey shopee - my package never arrived https://www.shopee.com/gp/css/order-history?ref_=nav_orders_first please fix asap! @shopeehelp"

text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)

print(text)
#Removing Unicode Characters


# In[7]:


text = "Hey Shopee - my package never arrived https://www.shopee.com/gp/css/order-history?ref_=nav_orders_first FIX THIS ASAP! @shopeeHelp"

text = text.lower()

print(text)
#text lower case


# In[8]:


text = "Hey Shopee - my package never arrived https://www.shopee.com/gp/css/order-history?ref_=nav_orders_first FIX THIS ASAP! @shopeeHelp"

text = text.upper()

print(text)
#text Upper Case

