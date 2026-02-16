name='Furkan'
surname='ÖZTÜRK'
age=26
print("My name is {} {} and I'm {} years old.".format(name,surname,age))# .format ile süslü parantez içerisine gelecek olan değişkeni seçebiliyoruz.
print("My name is {0} {1} and I'm {2} years old.".format(name,surname,age))
print("My name is {1} {0} and I'm {2} years old.".format(name,surname,age))
print("My name is {s} {n} and I'm {a} years old.".format(n=name,s=surname,a=age))
result=200/700
print(result)
print("the resul is {r:1.3}".format(r=result)) # burdaki 1 ifadesi kaç karakter boşluk bırakılarak yazılmaya başlansını gösterir.
                                               #3 ise virgülsen sonra kaç basamak yazılsın ve gerisi yuvarlansını gösterir
print(f"My name is {name} {surname} and I'm {age} years old.")
