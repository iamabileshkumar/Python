arr=[1,2,25,74,55]
rev=[]
n=len(arr)-1
#Method 1
print(arr[::-1])
#Method 2
for i in range(n,-1,-1):
    rev.append(arr[i])
print(rev)