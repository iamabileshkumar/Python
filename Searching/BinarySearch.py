def BinarySearch(arr,n):
    low=0
    high=len(arr)-1
    for i in range(len(arr)-1):
        mid=(low+high)//2
        if arr[mid]<n:
             low=mid+1
        elif arr[mid]>n:
             high=mid-1
        else:
             return mid
arr=[3, 5, 6, 42, 56]
print(f'we found the element at index :',BinarySearch(arr,42))
