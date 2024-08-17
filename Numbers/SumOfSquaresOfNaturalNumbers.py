num=int(input("Enter the Sum of Squares of Number:"))
sum=0
if num==0:
    print("0 is not a Natural Number")
else:
    for i in range(1,num+1,1):
        sum+=i**2
    print(sum, f'is a sum of Squares of Natural Number {num}')