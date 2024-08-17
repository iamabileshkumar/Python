def linearSearch(arr,n):
    for i in arr:
        if n==i:
            return arr[i]
    return -1

arr=[1,2,3,8,4,5]
n=int(input("Enter the Element to find"))
print(f'the element found at {linearSearch(arr,n)+1}')