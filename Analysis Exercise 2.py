#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

Location = "downloads/datasets/axisdata.csv"
df = pd.read_csv(Location)
df.head()


# In[2]:


df['Cars Sold'].mean()


# In[3]:


df['Cars Sold'].max()


# In[4]:


df['Cars Sold'].min()


# In[5]:


pd.pivot_table(df, values=['Cars Sold'], index=['Gender'])


# In[6]:


df[df['Cars Sold']>3]['Hours Worked'].mean()


# In[7]:


df['Years Experience'].mean()


# In[8]:


df[df['Cars Sold']>3]['Years Experience'].mean()


# In[9]:


pd.pivot_table(df, values=['Cars Sold'], index=['SalesTraining'])


# In[10]:


pd.pivot_table(df, values=['Cars Sold'], index=['Hours Worked'])


# In[12]:


pd.pivot_table(df, values=['Years Experience'], index=['Gender'])


# In[18]:


pd.pivot_table(df, values=['Hours Worked'], index=['Gender'])


# In[ ]:




