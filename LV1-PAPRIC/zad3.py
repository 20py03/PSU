br=0
sum=0
list=[]

while True:
    num=input('Unesite brojeve: ')
    br=br+1
    list.append(num)
    if num=="Done":
        list.pop()
        break
    try:
        num1=int(num)
    except:
        print('Nije broj!')
        continue
    sum=sum+num1
    av=sum/br
    list.sort()
print(br-1,av,min(list),max(list),list)
