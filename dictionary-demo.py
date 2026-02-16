ogrenciler={}
number=input("Öğrenci No: ")
name=input("Öğrenci Adı: ")
surname=input("Öğrenci Soyad: ")
phone=input("Öğrenci Telefon: ")

# ogrenciler[number]={
#     'ad':name,
#     'soyad':surname,
#     'telefon':phone
# }
ogrenciler.update({
    number:{
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})
print(ogrenciler)
