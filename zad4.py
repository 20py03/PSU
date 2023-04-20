import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ucitavanje ociscenih podataka
df = pd.read_csv('cars_processed.csv')
print(df.info())

sorted=df.sort_values(['selling_price'])
print(sorted)

auto2012 = len(df.loc[df['year'] == 2012])
print(auto2012)

sorted_km=df.sort_values(['km_driven'])
print(sorted_km)

sjedala = df['seats'].mode().iloc[0]
print(sjedala)

petrol=df[df.fuel == 'Petrol'].km_driven.mean()
dizel=df[df.fuel == 'Diesel'].km_driven.mean()
print(petrol)
print(dizel)


# razliciti prikazi
sns.pairplot(df, hue='fuel')

sns.relplot(data=df, x='km_driven', y='selling_price', hue='fuel')
df = df.drop(['name','mileage'], axis=1)

obj_cols = df.select_dtypes(object).columns.values.tolist()
num_cols = df.select_dtypes(np.number).columns.values.tolist()

fig = plt.figure(figsize=[15,8])
for col in range(len(obj_cols)):
    plt.subplot(2,2,col+1)
    sns.countplot(x=obj_cols[col], data=df)

df.boxplot(by ='fuel', column =['selling_price'], grid = False)

df.hist(['selling_price'], grid = False)

#tabcorr = df.corr()
#sns.heatmap(df.corr(), annot=True, linewidths=2, cmap= 'coolwarm') 

plt.show()


#1. U datasetu je dostupno 6699 automobila
#2. Tip pojedinog stupca u dataframeu je: object,int,float
#3. Najvecu cijenu ima:  BMW X7 xDrive 30d DPE, a najmanju: Maruti 800 AC
#4. 575 auta je proizvedeno u 2012. godini
#5. Najvise km je presao: Maruti Wagon R LXI Minor, a najmanje: Maruti Eeco 5 STR With AC Plus HTR CNG
#6. 5 sjedala
#7. Prosjecna prijeđena kilometraža sa benzinskim motorom je:54101.882809861534, a sa dizel motorom:88039.97234392114
