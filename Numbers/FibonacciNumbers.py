num=int(input("Enter the Number:"))
n1=0
n2=1
print(n1,end=' ')
print(n2,end=' ')
n3=0
for i in range(2,num):
    n3=n1+n2
    print(n3,end=' ')
    n1=n2
    n2=n3