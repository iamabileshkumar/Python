def LargestOfArray(n,arr):
    arr=sorted(arr)
    print(f'Largest Element is - {arr[-1]}')

n=int(input("Enter the Size of the Array:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the Element:")))
LargestOfArray(n,arr)