name='Furkan'
surname='ÖZTÜRK'
age=26

greeting='My Name is '+name+' '+surname+' and \n I am '+str(age)+' years old.'
length=len(greeting)
print(greeting[length-1])
print(greeting[0:9]) #0 'dan 9 a kadar olan indexler
print(greeting[0:40:2])#0'dan 40. indexe kadar 2 şer 2 şer atlayarak