a= input('Podaj nr swojego konta bankowego')
print("  ".join([a[i:i+4] if i>0 else a [0:2] for i in range(-2, 26, 4)]))

   
