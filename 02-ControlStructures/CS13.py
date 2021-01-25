x=5
y=2
print((f'Punkt P({x}, {y}) zanjduje sie w 1 cw') if (x>0 and y>0) else
     (f'Punkt P({x}, {y}) zanjduje sie w 2 cw') if (x<0 and y>0) else
     (f'Punkt P({x}, {y}) zanjduje sie w 3 cw') if (x<0 and y<0) else
     (f'Punkt P({x}, {y}) zanjduje sie w 4 cw') if (x>0 and y<0) else
     (f'Punkt P({x}, {y}) zanjduje sie na osi x') if x==0 and not y==0 else
     (f'Punkt P({x}, {y}) zanjduje sie na osi y') if (not x==0 and y==0) else
     (f'Punkt P({x}, {y}) zanjduje sie w srodku ukladu') if (x ==0and y==0) else'')