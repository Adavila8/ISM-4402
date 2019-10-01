#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "Downloads/datasets/gradedata.csv"
df = pd.read_csv(Location)

df.head()


# In[2]:


bins = [0,80,100]
status_names = ['Fail','Pass']
df ['Status'] = pd.cut(df['grade'], bins, labels= status_names)
df


# In[4]:


pd.value_counts(df['Status'])


# In[ ]:




