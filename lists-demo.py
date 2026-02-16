arabalar=['Mercedes','BMW','Opel','Mazda']
print(len(arabalar))
print(arabalar[0])
print(arabalar[len(arabalar)-1])
arabalar[-1]='Toyota'
print(arabalar)
print('Mercedes' in arabalar)
print(arabalar[0:3])
arabalar[-2:]='Totoya','Renault'
print(arabalar)
arabalar=arabalar+['Audi','Nissan']
print(arabalar)
del arabalar[-1]
print(arabalar)
print(arabalar[::-1])

studentA=['Yiğit','Bilgi',2010,[70,60,70]]
studentB=['Sena','Turan',1999,[80,80,70]]
studentC=['Ahmet','Turan',1998,[80,70,90]]

students=[studentA]+[studentB]+[studentC]
print(students)