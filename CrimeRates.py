
# coding: utf-8

# In[1]:

# A complete piece of code for building linear models for the crime rate data
# 03/06/2017 Haitian Xie


# In[2]:

import numpy as np
import pandas as pd
from sklearn import linear_model
from ggplot import *


# In[3]:

Data = pd.read_table(
    "/Users/haitianxie/Documents/Datasets/LinearRegressionModels/crime_rates.txt",
     delim_whitespace = True)
Data.head()


# In[8]:

y = Data.y.values.reshape(-1,1)
x = Data.x.values.reshape(-1,1)


# In[9]:

lm = linear_model.LinearRegression()
lm.fit(x,y)


# In[13]:

slope = np.round(np.asscalar(lm.coef_),3)
intercept = np.round(np.asscalar(lm.intercept_),3)
print("Each unit increase in x corresponds to %s units change in y." % slope)
print("y is estimated to be %s when x equals 0." % intercept)


# In[20]:

p = ggplot(aes(x = 'x', y = 'y'), data = Data)
p + geom_point() + geom_abline(slope=slope, intercept=intercept) + ggtitle("Crime Rate") + xlab("X") + ylab("Y")

