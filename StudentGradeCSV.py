#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location = "datasets/smallgradesh.csv"
df = pd.read_csv(Location, header=None)


# In[2]:


import pandas as pd
Location = "datasets/smallgradesh.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


df.columns = ['Names', 'Grades']
df.head()


# In[4]:


import pandas as pd
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df.head()


# In[5]:


import pandas as pd
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])
df.head()


# In[6]:


df.to_csv('studentgrades.csv',index=False,header=True)


# In[7]:





# In[ ]:




