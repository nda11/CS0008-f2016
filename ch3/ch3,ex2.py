length1=int(input('inter the length of the rectangle:'))
width1=int(input('inter the width of the rectangle:'))
length2=int(input('inter the length of the rectangle:'))
width2=int(input('inter the width of the rectangle:'))
area1=length1**2*width1**2
area2=length2**2*width2**2
if area1>area2:
    print('area1 has greater rectangle ')
elif area1<area2:
    print('area2 has greater rectangle ')
else:
    print(' both areas are equal')
