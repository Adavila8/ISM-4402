#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
grades = [76,95,77,78,99]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList, columns=['Names','Grades'])

writer =pd.ExcelWriter('datasets/dataframe.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name= 'Sheet1')
df.to_excel(writer, sheet_name= 'Sheet2')
writer.save()

