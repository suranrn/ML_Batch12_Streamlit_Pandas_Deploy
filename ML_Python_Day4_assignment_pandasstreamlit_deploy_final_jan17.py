#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings


# In[11]:


st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Iris_Dataset")


# In[7]:


#import dataset
df_iris = pd.read_csv("iris.data.csv", names=["sepal_length", "sepal_width", "petal_length", "petal_width", "class"])


# In[9]:


#First ten rows
iris_head = df_iris.head(10)


# In[10]:


#Display the table
st.table(iris_head)
st.header("Visualisation Using Seaborn")


# In[14]:


#table description
st.subheader("Iris Dataset summary")


# In[13]:


df_iris.describe()


# In[15]:


iris_describe = df_iris.describe()


# In[27]:


st.table(iris_describe)


# In[17]:


df_iris.groupby("class").size()


# In[18]:


st.table(df_iris.groupby("class").size())


# In[19]:


st.subheader("Iris Dataset plants (class) summary")


# In[20]:


st.subheader("Iris setosa")


# In[21]:


st.table(df_iris[df_iris["class"] == "Iris-setosa"].describe())


# In[22]:


st.subheader("Iris versicolor")


# In[23]:


st.table(df_iris[df_iris["class"] == "Iris-versicolor"].describe())


# In[24]:


st.subheader("Iris virginica")


# In[26]:


st.table(df_iris[df_iris["class"] == "Iris-virginica"].describe())


# In[ ]:





# In[28]:


st.subheader("Count Plot for Class")


# In[29]:


sns.countplot(x = "class",data = df_iris)


# In[30]:


st.pyplot()


# In[36]:


st.subheader("Distribution Plots")
st.subheader("Petal Length")
sns.distplot(df_iris['petal_length'])
st.pyplot()


# In[38]:


st.subheader("Petal Width")
sns.distplot(df_iris['petal_width'])
st.pyplot()


# In[39]:


st.subheader("Sepal Length")
sns.distplot(df_iris['sepal_length'])
st.pyplot()


# In[41]:


st.subheader("Sepal Width")
sns.distplot(df_iris['sepal_width'])
st.pyplot()


# In[53]:


#bar plot
#st.subheader("Bar Plot")
#df_iris.plot(kind='bar')
#st.pyplot()


# In[54]:


st.subheader("Bar Plot for class *Iris setosa*")
df_iris[df_iris['class'] == "Iris-setosa"].plot(kind='bar')
st.pyplot()


# In[57]:


st.subheader("Bar Plot for class *Iris versicolor*")
df_iris[df_iris['class'] == "Iris-versicolor"].plot(kind='bar')
st.pyplot()


# In[56]:


st.subheader("Bar Plot for class *Iris virginica*")
df_iris[df_iris['class'] == "Iris-virginica"].plot(kind='bar')
st.pyplot()


# In[42]:


st.subheader("Bar Plots")
st.subheader("Sepal Length")
sns.barplot(x = "class", y = "sepal_length", data = df_iris)
st.pyplot()


# In[43]:


st.subheader("Petal Length")
sns.barplot(x = "class", y = "petal_length", data = df_iris)
st.pyplot()


# In[44]:


st.subheader("Box Plots")
st.subheader("Sepal_width")
sns.boxplot(x="class", y="sepal_width", data=df_iris,palette='Set1')
st.pyplot()


# In[45]:


st.subheader("Petal_width")
sns.boxplot(x="class", y="petal_width", data=df_iris,palette='rainbow')
st.pyplot()


# In[46]:


st.subheader("Box Plot for Petal width vs Petal length for all Plants *(class)*")
sns.boxplot(x="petal_width", y="petal_length", data=df_iris,palette='Set1',hue='class')
st.pyplot()


# In[47]:


st.subheader("Strip Plot *(petal width vs petal length)*")

sns.stripplot(x="petal_width", y="petal_length", data=df_iris,jitter=True,hue='class',palette='Set1')
st.pyplot()


# In[49]:


st.subheader("Swarm Plot *(sepal width vs sepal length)*")

sns.swarmplot(x="sepal_width", y="sepal_length",hue='class',data=df_iris, palette="Set1", dodge=True)
st.pyplot()


# In[50]:


st.subheader("Paiplot for Iris dataset *(class as hue)*")

sns.pairplot(df_iris,hue='class',palette='rainbow')
st.pyplot()


# In[51]:


st.subheader("Correlation matrix for Iris dataset")
st.table(df_iris.corr())


# In[52]:


st.subheader("Heatmap")
sns.heatmap(df_iris.corr(),cmap='coolwarm',annot=True)
st.pyplot()


# In[ ]:




