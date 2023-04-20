import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, max_error

df=pd.read_csv('cars_processed.csv')
df=df.drop(['name'],axis=1)
df = pd.get_dummies(df,columns=['fuel','transmission','seller_type','owner'],drop_first=True)
print(df)
x = df.drop('selling_price',axis=1)
y =  df['selling_price']
scaler = StandardScaler()
x = scaler.fit(x).transform(x.astype(float))
print(x)
train, test, train_cijena, test_cijena = train_test_split(x,y, test_size = 0.05)
stupanj_dva = PolynomialFeatures(2)
train_stupanj_dva = stupanj_dva.fit_transform(train)
lr = linear_model.LinearRegression()
lr.fit(train_stupanj_dva, train_cijena)
test_stupanj_dva = stupanj_dva.fit_transform(test)
y_test = lr.predict(test_stupanj_dva)
print("R2: ",r2_score(test_cijena,y_test))
print("Srednja apsolutna pogreska: ",mean_absolute_error(test_cijena,y_test))
print("Srednja kvadratna pogreska: ",mean_squared_error(test_cijena,y_test))
print("Najveca pogreska: ",max_error(test_cijena,y_test))
