def split1(arr,n):
    c=arr[n:]+arr[:n]
    return c

arr1=[1,2,34,85,5]
print(split1(arr1,2))