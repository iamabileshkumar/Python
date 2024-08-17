def BubbleSort():
    arr=[3,42,56,5,6]
    for i in range(0,len(arr)-1):
                for j in range(len(arr)-i-1):
                    if arr[j]<arr[j+1]:
                        pass
                    else:
                        temp=arr[j]
                        arr[j]=arr[j+1]
                        arr[j+1]=temp
    return arr

print(f'The sorted Array is :',BubbleSort())

