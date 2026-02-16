names=['Ali','Yağmur','Hakan','Deniz']
years=[1998,2000,1998,1987]
names.append('Cenk')
names.insert(0,'Sena')
print(names.index('Deniz'))
names.remove('Deniz')
print(names.__contains__('Ali'))
names.sort()
years.sort()
print(years)
print(names[::-1])
print(names)
str="Chevrolet,Dacia"
arabalar=str.split(',')
print(arabalar)
print(f'En büyük sayı: {max(years)} En küçük sayı: {min(years)}')
print(years.count(1998))
years.clear()
print(years)
markalar=[]
marka=input("Marka: ")
markalar.append(marka)
print(markalar)