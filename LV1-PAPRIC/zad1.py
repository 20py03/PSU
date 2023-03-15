def total_euro(sati,euri):
    return sati*euri

sati_rada=int(input('Unesite sate rada: '))
zarada=int(input('Unesite zaradu po satu: '))
print('Ukupna zarada je: ',total_euro(sati_rada,zarada),'EUR') 