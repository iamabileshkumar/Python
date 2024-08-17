num=int(input("Enter the Number"))
c=65
for i in range(1,num+1):
    a=chr(c)
    for j in range(i):
        
        print(a,end=" ")
    c+=1
    print(end="\n")