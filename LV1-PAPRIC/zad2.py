try:
    ocjena=float(input('Unesite Vas podatak: '))
except:
    print('Unos je izvan moguceg intervala')
while(ocjena<0.0 or ocjena>1.0):
    ocjena=float(input('Pokusajte opet: '))

if(ocjena<0.6):
    print('F')
elif(ocjena>=0.6 and ocjena<0.7):
    print('D')
elif(ocjena>=0.7 and ocjena<0.8):
    print('C')
elif(ocjena>=0.8 and ocjena<0.9):
    print('B')
elif(ocjena>=0.9):
    print('A')