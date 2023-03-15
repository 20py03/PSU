br=0
sum=0
name=input('Unesite ime datoteke: ')
fhand=open(name)
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        br=br+1
        pos=line.find(':')
        num=float(line[pos+1:])
        sum=sum+num
print('Srednja vrijednost pouzdanosti: ',sum/br)
