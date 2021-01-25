a = int(input('podaj dl boku 1 '))
b = int(input('podaj dl boku 2 '))
c = int(input('podaj dl boku 3 '))
p = (((a+b+c) * (a+b-c) * (a-b+c) * (-a+b+c)) ** (1/2)) / 4
print (f'pole trojkata dla wielkosci bokow {a}, {b}, {c} wynosi {p}')
        
    