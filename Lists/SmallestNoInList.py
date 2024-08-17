arr=[8,5.4,3,88,44,1,11,00]
print('Min Element-%d'%min(arr))
#Method 2
min=arr[0]
for i in arr:
    if min>i:
        min=i
print('Min Element-%d'%min)