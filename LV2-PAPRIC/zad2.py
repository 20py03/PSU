import numpy as np
import matplotlib.pyplot as plt
 
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)
 
x= []
y= []
weight= []
cyl= []
for i in data:
    x.append(i[0])
    y.append(i[3])
    weight.append(12*i[5])
    cyl.append(i[1])
print(x)
print(y)
plt.scatter(x,y,s=weight,c='blue',alpha=1)
plt.xlabel('Potrosnja automobila(mpg)')
plt.ylabel('Konjske snagee(hp)')
plt.title('Drugi zadatak')
 
cyl6= []
j=0
for i in cyl:
    if(i==6):
        cyl6.append(x[j])
    j+=1
 
print('Minimalna potrosnja automobila(mpg): ',min(x))
print('Maksimalna potrosnja automobila(mpg): ',max(x))
print('Srednja vrijednost automobila(mpg): ',sum(x)/len(x))
 
print('Minimalna potrosnja automobila(mpg): ',min(cyl6))
print('Maksimalna potrosnja automobila(mpg): ',max(cyl6))
print('Srednja vrijednost automobila(mpg): ',sum(cyl6)/len(cyl6))
plt.show()