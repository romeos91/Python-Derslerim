def changeName(n):
    n='Furkan'

name='Rıdvan'

changeName(name)
print(name)

# Burada fonksiyona bir parametre göndermemize rağmen bellekte farklı yerlerde tutulmalarından ötürü Rıdvan bilgisi bize dönecektir.

def change(n):
    n[0]='İstanbul'

sehirler=['Ankara','İzmir']
change(sehirler) 
print(sehirler)   

# Burada ise ankara değerinin İstanbul ile değiştiğini görüyoruz. Listelerin adres için aynı referansı kullanma muhabbeti yüzünden.

def add(*params):
    return sum((params))

print(add(10,20,30,4))
print((add(1,2,3,4,5)))

def displayUsers(**params):
    for key,value in params.items():
        print('{} is {}'.format(key,value))



displayUsers(name='Furkan',age=26,city='Sakarya')
displayUsers(name='Rıdvan',age=26,city='Tekirdağ')
displayUsers(name='Numan',age=24,city='Yalova')                