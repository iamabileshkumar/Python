
def SumOfArray(n,arr):
    sum=0
    for i in arr:
        sum+=i
    return sum

n=int(input("enter the no of elements in array:"))
arr=[]
for i in range(n):
    arr.append(int(input("enter the element")))
print(f'the sum of the array is {SumOfArray(n,arr)}')