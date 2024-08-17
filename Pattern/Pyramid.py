num=int(input("Enter the Number 0f rows:"))
for i in range(1,num+1):
    for k in range(num,i,-1):
        print('',end=' ')
    for j in range(i):
        print('*',end=' ')
    print('',end='\n')