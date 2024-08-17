def prime(Num):
    pr=[]
    nr=[]
    for j in Num:
        if j>1:
                flag=0
                for i in range(2,j):
                    if (j%i)==0:
                        flag=1
                        break
                if(flag==1):
                    nr.append(j)
                else:
                    pr.append(j)  
        else:
            print("prime can\'t be a Negative Number")
        j=j+1  
    return pr,nr

Prime,NonPrime=prime([7,7,6,2,3,5,19,54,34,319,4783,47577])
print(f'Prime Number - {Prime}','\nNon Prime Numbers - %ls'%NonPrime)

            