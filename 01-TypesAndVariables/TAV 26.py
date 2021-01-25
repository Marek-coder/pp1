a = int(input('podaj wzrost w cm'))
b = int(input('podaj wage w kg'))
BMI = (b/((a/100)**2))
print(f'wskaznik BMI wynosi{BMI}', '(waga prawidlowa)' if 25>BMI>18.5 else '(waga nieprawidlowa)')