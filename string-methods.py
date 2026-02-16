message="Hello There. My Name is Furkan Öztürk"
print(message.upper())
print(message.lower())
print(message.title()) # her kelimenin baş harfi büyük
print(message.capitalize()) # sadece metnin ilk harfi büyük
message2="    Hello There. My Name is Furkan Öztürk"
print(message2.strip()) #baştaki boşluk karakterlerini siler
print(message.split()) # her bir kelimeyi ayırıp dizi olarak yazar
print(message.split(".")) # noktalardan ayırır. yani cümle ayırır
ayrık_mesaj=message.split()
print(" ".join(ayrık_mesaj)) # birleştirir. birleştirme şekli en başta boşluk olarak verilmiş örnek olarak.
index=message.find("Furkan")#verilen kelimeyi metnin içinde arar ve eğer var ise başladığı index numarasını döndürür.
print(index)
print(message.center(50,'*'))#verilen sayı(50) kadar bir alan ayırır ve verdiğimiz değişken ile o alanı doldurur. metni tam ortaya koyar.