import pandas as pd

mtcars=pd.read_csv('mtcars.csv')

#1
max_potrosnja=mtcars.sort_values (by=['mpg']).head(5)
print(max_potrosnja)

#2
min_potrosnja=mtcars.sort_values (by=['mpg'])
osam_cyl=min_potrosnja[(mtcars.cyl==8)].tail(3)
print(osam_cyl)

#3
sest_cyl=mtcars[mtcars['cyl']==6]
avg_potrosnja=sest_cyl['mpg'].mean()
print(avg_potrosnja)

#4
cetiri_cyl=mtcars[mtcars['cyl']==4]
avg_potrosnja_masa=cetiri_cyl[(cetiri_cyl.wt>=2.000) & (cetiri_cyl.wt<=2.200)]['mpg'].mean()
print(avg_potrosnja_masa)

#5
rucni=mtcars[mtcars.am==1]['car'].count()
automatski=mtcars[mtcars.am==0]['car'].count()
print('Rucni mjenjac ima ',rucni,' automobila')
print('Automatski mjenjac ima ',automatski,' automobila')

#6
preko_sto=mtcars[(mtcars.am==1) & (mtcars.hp>100)]['car'].count()
print('Broj automobila s automatskim mjenjacem i snagom preko 100 konjskih snaga: ',preko_sto)

#7
mtcars['kg']=mtcars['wt']*0.45359
print(mtcars[['car','kg']])
