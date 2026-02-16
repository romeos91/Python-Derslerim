website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sonra Python Programlama Rehberiniz (40 saat)"

length=len(course)
print(length)

print(website[7:10]) # "www" ifadesi
print(website[len(website)-3:len(website)]) # "Com" ifadesi
print(course[:15]) #ilk 15 karakter
print(course[len(course)-15:len(course)]) #son 15 karakter
print(course[-15:]) #yukarıdaki ile aynı şey. son 15 karakter.
print(course[::-1]) # ifadeyi tersten yazdır birinci nokta başlangıç. ikinci nokta sonu. üçüncü nokta ise yani -1 tersten yazması için

name,surname,age,job="Furkan","ÖZTÜRK",26,"Mühendis"
print(f"Benim adım {name} {surname},Yaşım {age},Ve mesleğim {job}")

Greeting="Hello world"
Greeting=Greeting.replace('w','W')
print(Greeting)
yazi='abc'
print(yazi*3)
