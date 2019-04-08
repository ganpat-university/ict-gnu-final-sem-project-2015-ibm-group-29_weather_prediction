#!/usr/bin/env python
# coding: utf-8

# In[47]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns

df = pd.read_csv('D:\\IBM Project\\Weather Prediction\\Test Data\\Testclean2.csv')


# In[48]:


print(df.head(5))


# In[49]:


print(df['_conds'].head(5))
print(df['_wdire'].head(5))


# In[50]:


print(pd.get_dummies(df['_conds']).head(5))
print(pd.get_dummies(df['_wdire']).head(5))


# In[51]:


for col_name in df.columns:
    if df[col_name].dtypes == 'object':
        unique_cat = len(df[col_name].unique())
        print("Feature '{col_name}' has {unique_cat} unique categories".format(col_name=col_name, unique_cat=unique_cat))


# In[52]:


print(df['datetime_utc'].value_counts().sort_values(ascending=False).head(10))


# In[53]:


df.isnull().sum().sort_values(ascending=False).head()


# In[33]:


plt.rcParams['figure.figsize'] = [14, 8]  
df._dewptm.hist()  
plt.title('Distribution')  
plt.xlabel('_dewptm')  
plt.show()  


# In[55]:


print(df.head(5))


# In[46]:





# In[ ]:





# In[ ]:





# In[ ]:




