
class Person:
  #  pass # hata vermemesi için yer doldursun diye pass yazabiliriz.
 #   def karsila(self,name):
 #     print(f'Hoş geldin {name}')
 

  def __init__(self,name,year):
    # Consturactor Yapıcı metot
    self.name=name
    self.year=year
    print("Kullanıcı oluşturuldu")
    print(name,year)


  def intro(self):
   print(f"Hello There! I'm {self.name}")



p1=Person('Furkan',1999)
p2=Person('Ahmet',2000)
p1.intro()
p2.intro() 



