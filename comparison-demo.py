vize=float(input("Vize Notunuz: "))
final=float(input("Final Notunuz: "))
toplam=(vize*0.4)+(final*0.6)
if(toplam>=50):
    print("Geçtiniz!... \nNotunuz: ",toplam)
else:
    print("Kaldınız!...\nNotunuz: ",toplam)
