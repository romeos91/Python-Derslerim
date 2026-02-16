def square(num):
    return num**2

numbers=[1,3,5,7,9]
result=list(map(square,numbers)) 
print(result)
# Burada square metodumuza for döngüsüne gerek olmadan map yardımıyla bir liste gönderdik ve elemanlarımızın karesini alıp geri döndürdü.

numbers2=[1,3,5,7,9]
result2=list(map(lambda num:num**2,numbers2))
print(result2)

# Burda da yine map yapısı kullandık fakat fonksiyon adı vermeden, lambda kullanarak bu işlemi gerçekleştirdik.