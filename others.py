x=y=[1,2,3]
z=[1,2,3]
print(x==y) 
print(x==z)
print(x is y) # Burada adres referanslarını karşılaştırır. x ve y aynı referansa sahipken z farklıdır bu yüzden x is z false döndürecektir.
print(x is z)