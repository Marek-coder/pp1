for x in range(1,31):
    if not x % 5 and not x % 3:
        print('BINGO')
    elif not x % 5 and x % 3:
        print('five')
    elif not x % 3 and x % 5:
        print('three')
    else:
        print (x)
    