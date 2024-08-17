arr=[4,1,3,9,7]
c=0
for i in range(0,len(arr)-1):
    temp=arr[i]
    for j in range(i+1,len(arr)):
        if temp>arr[j]:
            temp=arr[j]
            c=j
    if arr[i]>temp:
        swap=arr[i]
        arr[i]=arr[c]
        arr[c]=swap
print(arr)