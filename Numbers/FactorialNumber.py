num=int(input("Enter the Number"))
fact=1
if num<0:
    print("Factorial Can\'t be Negative Number")
else:
    while(num>0):
        fact*=num
        num-=1
print(f'Factorial is {fact}')