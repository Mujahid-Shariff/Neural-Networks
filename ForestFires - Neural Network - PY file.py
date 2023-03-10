# -*- coding: utf-8 -*-
"""forestfires_Neural_Networks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CR0IFGucqF_JxgJ5i8SSKznbWWY2vVSi
"""

from google.colab import files
uploaded=files.upload()

# Importing the data
import pandas as pd
df=pd.read_csv("forestfires.csv")
df.head()

# Get information of the dataset
df.info()
print('The shape of our data is:', df.shape)
df.isnull().any()
df.dtypes

"""**Data Visvualization & EDA (Exploratory Data Analysis)**"""

# let's scatter plot to visualise the attributes all at once
import seaborn as sns
sns.pairplot(data = df, hue = 'size_category')

# Boxplot
df.boxplot(column="size_category", vert=False)

# Histogram
df["size_category"].hist()

# Bar graph
df.plot(kind="bar")

# Heatmap
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(12,8))
heatmap_y_month = pd.pivot_table(data=df,values="size_category",index="day",columns="month",fill_value=0)
sns.heatmap(heatmap_y_month,annot=True,fmt="g") #fmt is format of the grid values

# Label Encoding
from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
df['month']=LE.fit_transform(df['month'])
df['day']=LE.fit_transform(df['day'])
df['size_category']=LE.fit_transform(df['size_category'])
df

# Split the input as X and Y variables
X = df.iloc[:,0:30]
Y = df["size_category"]
X.shape

# Import the libraries
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

# Model fitting
model=Sequential()
model.add(Dense(45, input_dim=30, activation ='relu')) #input layer 45 = 30*1.5 as Neurons we are adding #hidden layer 1
model.add(Dense(68, input_dim=45, activation ='relu')) #i can add another hidden layer for the data to improve our underfit or overfit,#hidden layer 2
model.add(Dense(1,activation ="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer='adam', metrics=['MeanSquaredError'])

history=model.fit(X,Y, validation_split=0.3, epochs=250, batch_size=10)

scores=model.evaluate(X,Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

history.history.keys()

# Summarize history for accuracy
import matplotlib.pyplot as plt
plt.plot(history.history['mean_squared_error'])
plt.plot(history.history['val_mean_squared_error'])
plt.title('model accuracy')
plt.ylabel('MeanSquaredError')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper right')
plt.show()