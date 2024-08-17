a=[1,2,3,5,68,7,7,88,345,9,0,4,5]
b=a[0:len(a)]
print(f'b1-{b}')
#or
b=a[:]
print(f'b2-{b}')
#or
b=[]
for i in a:
    b.append(i)
print(f'b3-{b}')