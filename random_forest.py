def accuracy(precipitation,temp_max,temp_min,wind,weather):
	import numpy as np
	import matplotlib.pyplot as plt
	import pandas as pd
	import seaborn as sns
	import warnings
	warnings.filterwarnings("ignore")

	ds=pd.read_csv('E:/weather_project/seattle-weather.csv')
	ds


	sns.heatmap(ds.isnull())
	ds1=ds.dropna()



	sns.heatmap(ds1.isnull())


	#seattle-weather.csv
	x=ds1[['precipitation','temp_max','temp_min','wind']].values 
	y=ds1[['weather']].values





	from sklearn.model_selection import train_test_split
	x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)


	print("no of rows,column",x.shape)
	print("x_train",x_train.shape)
	print("x_test",x_test.shape)
	print("y_train",y_train.shape)
	print("y_test",y_test.shape)

	from sklearn.ensemble import RandomForestClassifier
	model=RandomForestClassifier(n_estimators=95)


	model.fit(x_train,y_train)


	model.score(x_test,y_test)*100


	y_predict=model.predict(x_test)


	y_test=y_test.reshape(-1,1)
	y_pred=y_predict.reshape(-1,1)

	df=np.concatenate((y_test,y_pred),axis=1)
	dataframe=pd.DataFrame(df,columns=['current weather','prediction of weather'])

	dataframe


	from sklearn.metrics import confusion_matrix
	cm=confusion_matrix(y_test,y_pred)

	cm=confusion_matrix(y_test,y_pred)
	sns.heatmap(cm,annot=True)
	plt.xlabel("predicted")
	plt.ylabel("true")


	ds1.tail()


	tp1=ds1.iloc[0:1460]
	tp1


	
	x2=tp1[['precipitation','temp_max','temp_min','wind']].values 
	y2=tp1[['weather']].values


	x2


	y2


	# this is the portion we need to change
	#tp=ds1.tail(1)#iloc[1460:1461]
	#tp
	#print(tp)

	# In[69]:


	x1=[[precipitation,temp_max,temp_min,wind]] #tp[['precipitation','temp_max','temp_min','wind']].values 
	y1=[[weather]]#tp[['weather']].values

	print("this is x1 ",x1)
	print("this is y1 ",y1)
	# In[70]:


	x1


	# In[71]:


	y1


	# In[72]:


	print("x_train",x2.shape)
	#print("x_test",x1.shape)
	print("y_train",y2.shape)
	#print("y_test",y1.shape)


	# In[73]:


	model.fit(x2,y2)


	# In[74]:


	model.score(x1,y1)*100


	# In[75]:


	y_predict1=model.predict(x1)


	# In[76]:


	#y1=y1.reshape(-1,1)
	y1_pred=y_predict1.reshape(-1,1)


	# In[77]:


	y_predict1


	# In[78]:


	#y1_pred=y_predict1.reshape(-1,1)
	#tp=np.concatenate((y1,y1_pred),axis=1)
	#dataframe1=pd.DataFrame(tp,columns=['current weather','prediction of weather'])


	# In[79]:


#dataframe1


	# In[80]:

	global finalaccuracy
	print("you can expect :")

	if y1_pred==1:
		#print("drizzle")
		finalaccuracy="drizzle"
	elif y1_pred==2:
		finalaccuracy="rainy/cloudy"
	elif y1_pred==3:
		finalaccuracy="sunny"
	elif y1_pred==4:
		finalaccuracy="snowy"
	elif y1_pred==5:
		finalaccuracy="foggy"    

	
	return finalaccuracy


#print(accuracy(weather))

