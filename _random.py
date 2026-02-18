import random
# value=dir(random)
# print(value)
# print(help(random))

# result=random.random() *100
result=int(random.uniform(1,100))
result2=random.randint(1,100)
print(result)
print(result2)
names=["Ali","Veli","Ayşe","Fatma"]
result3=random.choice(names) # listeden rastgele bir eleman seçer
print(result3) 