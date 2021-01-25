import random
a=int(input('Podaj jaka liczbe wyrzucil komputer'))
b= random.randint(1, 6)
print(f'komputer wyrzucil {b}')
print(f'(zgadles)' if a==b else '(nie zgadles)')


