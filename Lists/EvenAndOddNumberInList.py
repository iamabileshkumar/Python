num=int(input("Enter the number of elements you want to add in your List: "))
arr=[]
Even=[]
odd=[]
for i in range(num):
    arr.append(int(input()))
for j in arr:
    if j%2==0:
        Even.append(j)
    else:
        odd.append(j)
print(f'Even Numbers are - {Even}')
print(f'Odd Numbers are - {odd}')