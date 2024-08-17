def monotonic(arr,n):
    c=0
    for i in range(n-1):
            if arr[i]>=arr[i+1]:
                c+=1
            else:
                c-=1
    if c==n-1:
        return True
    else:
        return False

arr=[6,5,4,4,1]
arr2=[3,4,6,2,1]
print(monotonic(arr,len(arr)))
print(monotonic(arr2,len(arr)))