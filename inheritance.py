class Person():
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print(f"Kullanıcı oluşturuldu: {self.fname} {self.lname}")

p1=Person("Furkan","Kaya")

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
        print(f"Öğrenci oluşturuldu: {self.fname} {self.lname}")
s1=Student("Ahmet","Yılmaz")