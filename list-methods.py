numbers=[1,3,6,2,1,9,16,8]
letters=['a','b','y','e','a','c']
print(min(numbers))
print(max(numbers))
print(max(letters))
print(numbers[3:6])
numbers[4]=40
numbers.append(49) # listenin sonuna ekleme yapar
numbers.insert(0,31)

popped=numbers.pop() # stack mantığı ile aynı, son elemanı alır ve listeden çıkarır
print(popped)
popped_with_index=numbers.pop(3)# 3. indexteki elemanı pop eder
print(numbers)
print(popped_with_index)
numbers.remove(31)
print(numbers)