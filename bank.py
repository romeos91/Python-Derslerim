# Senaryo: Bir bankanın kredi onay mekanizmasını kodlamalısınız. Sistemin kararı şu kriterlere bağlı olmalı:
# Kredi Skoru: 0-1000 arası. (700 altı doğrudan ret).
# Aylık Gelir: Kredi taksitinin en az 3 katı olmalı.
# Mevcut Borç Durumu: Gelirin %40'ından fazlası borçtaysa ret.
# Yaş: 18-65 arası olmalı.
# Ek Koşul: Eğer kredi skoru 900 üzerindeyse, gelir şartı 2.5 kata düşebilir.
# Sizden Beklenen: Kullanıcıdan bu verileri alıp, her bir adımı kontrol eden ve reddedilme durumunda "reddedilme sebebini"
# (örneğin: "Kredi skorunuz yetersiz" veya "Borç oranınız çok yüksek") spesifik olarak belirten bir algoritma kurmanız.

print("Öztürk BANK'a hoşgeldiniz, Lütfen 4 haneli şifrenizi giriniz:")
while True:
    sifre=input()
    if not sifre.isdigit():
        print("Lütfen sadece sayı giriniz")
        continue
    elif len(sifre)!=4:
        print("Lütfen 4 haneli şifre giriniz")
        continue    
    elif sifre=="9636":
        print("Giriş başarılı, Kredi ekranına yönlendiriliyorsunuz...")
        break

class Kullanıcı:
 def __init__(self,kredi_skor,aylik_gelir,guncel_borc,yas,vade,kredi_miktari):
            self.kredi_skor=kredi_skor
            self.aylik_gelir=aylik_gelir
            self.guncel_borc=guncel_borc
            self.yas=yas
            self.vade=vade
            self.kredi_miktari=kredi_miktari
            self.kredi_taksidi=kredi_miktari/vade

 def kredi_sorgula(self):
        if self.yas<18 or self.yas>65:
            return "Kredi Başvurusu Reddedildi: Yaşınız 18-65 arasında olmalıdır"
        if self.guncel_borc>self.aylik_gelir*0.4:
            return "Kredi Başvurusu Reddedildi: Mevcut borcunuz aylık gelirinizin %40'ından fazla"
        if self.kredi_skor<700:
            return "Kredi Başvurusu Reddedildi: Kredi skorunuz en az 700 olmalıdır"
        if self.kredi_skor>=900: 
            gelirbaraji=2.5
        else:
            gelirbaraji=3
        if self.aylik_gelir<self.kredi_taksidi*gelirbaraji:
         return f"Kredi Başvurusu Reddedildi: Aylık geliriniz taksidin en az {gelirbaraji} katı olmalıdır. (Gereken: {self.kredi_taksidi * gelirbaraji} TL)"
        return "Kredi başvurunuz onaylandı"

print("Kredi durumunuzu sorgulamak için lütfen aşağıdaki bilgileri giriniz:\n")
def input_al(mesaj,min_deger,max_deger):
    while True:
     try:
      deger=int(input(mesaj))
      if deger<min_deger or deger>max_deger:
         print(f"Lütfen {min_deger} ile {max_deger} arasında bir değer giriniz.")
         continue
      return deger
     except ValueError:
      print("Lütfen geçerli bir sayı giriniz.")

kredi_skor=input_al("Kredi Skorunuz (0-1000): ",0,1000)
aylik_gelir=input_al("Aylık Geliriniz: ",0,float('inf'))
guncel_borc=input_al("Mevcut Borç Durumunuz: ",0,float('inf'))
yas=input_al("Yaşınız (18-120): ",18,120)
vade=input_al("Kredi vadesi (1-48 ay): ",1,48)
kredi_miktari=input_al("Kredi Miktarı: ",1,float('inf'))

kullanici=Kullanıcı(kredi_skor,aylik_gelir,guncel_borc,yas,vade,kredi_miktari)
print(kullanici.kredi_sorgula())