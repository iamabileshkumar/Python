num=int(input("Enter the Number of Lines"))
c=1
for i in range(1,num+1):
    for j in range(i):
        print(c,end=" ")
        c+=1
    print(end="\n")