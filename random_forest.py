import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# In[8]:


ds=pd.read_csv('E:\weather_project\seattle-weather.csv')
ds


# In[9]:


sns.heatmap(ds.isnull())
ds1=ds.dropna()


# In[10]:


sns.heatmap(ds1.isnull())


# In[12]:


#predict
#x=ds1[['MinTemp','MaxTemp','Rainfall','Evaporation','Sunshine','WindGustSpeed','WindSpeed9am','Humidity3pm','Pressure9am','Pressure3pm','Cloud9am','Cloud3pm','Temp9am','Temp3pm',]].values #iloc[:,:-1].values
#y=ds1[['RainToday','RainTomorrow']].values

	from sklearn.ensemble import RandomForestClassifier
	model=RandomForestClassifier(n_estimators=95)


#seattle-weather.csv
x=ds1[['precipitation','temp_max','temp_min','wind']].values 
y=ds1[['weather']].values


# In[13]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


# In[14]:


print("no of rows,column",x.shape)
print("x_train",x_train.shape)
print("x_test",x_test.shape)
print("y_train",y_train.shape)
print("y_test",y_test.shape)


# In[15]:


x_train


# In[16]:


y_train


# In[17]:


from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=95)


# In[18]:


model.fit(x_train,y_train)


# In[19]:


model.score(x_test,y_test)*100


# In[20]:


y_predict=model.predict(x_test)


# In[21]:


y_test=y_test.reshape(-1,1)
y_pred=y_predict.reshape(-1,1)


# In[22]:



df=np.concatenate((y_test,y_pred),axis=1)
dataframe=pd.DataFrame(df,columns=['current weather','prediction of weather'])


# In[23]:


dataframe


# In[24]:


from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)


# In[25]:


cm=confusion_matrix(y_test,y_pred)
sns.heatmap(cm,annot=True)
plt.xlabel("predicted")
plt.ylabel("true")


# In[26]:


ds1.tail()


# In[64]:


tp1=ds1.iloc[0:1460]
tp1


# In[65]:


x2=tp1[['precipitation','temp_max','temp_min','wind']].values 
y2=tp1[['weather']].values


# In[66]:


x2


# In[67]:


y2


# In[68]:

# this is the portion we need to change
tp=ds1.iloc[1460:1461]
tp


# In[69]:


x1=tp[['precipitation','temp_max','temp_min','wind']].values 
y1=tp[['weather']].values


# In[70]:


x1


# In[71]:


y1


# In[72]:


print("x_train",x2.shape)
print("x_test",x1.shape)
print("y_train",y2.shape)
print("y_test",y1.shape)


# In[73]:


model.fit(x2,y2)


# In[74]:


model.score(x1,y1)*100


# In[75]:


y_predict1=model.predict(x1)


# In[76]:


y1=y1.reshape(-1,1)
y1_pred=y_predict1.reshape(-1,1)


# In[77]:


y_predict1


# In[78]:


y1_pred=y_predict1.reshape(-1,1)
tp=np.concatenate((y1,y1_pred),axis=1)
dataframe1=pd.DataFrame(tp,columns=['current weather','prediction of weather'])


# In[79]:


dataframe1


# In[80]:


print("the current weather is :")

if y1_pred==1:
    #print("drizzle")
    finalaccuracy="drizzle"
elif y1_pred==2:
    finalaccuracy="rainy"
elif y1_pred==3:
    finalaccuracy="sunny"
elif y1_predict==4:
    finalaccuracy="snowy"
elif y1_pred==5:
    finalaccuracy="foggy"    

def accuracy():
	global finalaccuracy
	return finalaccuracy


print(accuracy())

