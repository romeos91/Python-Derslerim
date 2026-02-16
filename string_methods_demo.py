website="http://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

message='     Hello World    '
print(message.strip()) #lstrip sol boşlukları rstrip ise sağ boşlukları siler. strip ise hem sağ hem sol
site="www.sadikturan.com"
print(site.strip('w.com'))
print(course.lower())
print(website.count('a'))
print(website.startswith('www.'))
print(website.endswith('.com'))
print(website.__contains__('.com'))
print(course.isalpha())
result='Contents'
print(result.center(50,'*'))
print(course.replace(' ','-'))
message=message.replace('World','There')
print(message)
ayrık=course.split()
print("".join(ayrık))
