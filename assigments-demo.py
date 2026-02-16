x,y,z=2,5,10
numbers=1,5,7,10,6

# sayi1=input("1.Sayi: ")
# sayi2=input("2.Sayi: ")
# sayi1=int(sayi1)
# sayi2=int(sayi2)
# print((sayi1*sayi2)-(x+y+z))
print(y//x)
print((x+y+z)%3)
print(y**x)

x,*y,z=numbers # numbersin ilk indexini x'e atar, son indexini z'ye atar. geri kalan ortadaki değerleri ise y'ye atar. y artık bir dizi olur.
print(y)