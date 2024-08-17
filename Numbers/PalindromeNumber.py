num=int(input("Enter the input:"))
temp=num
rev=0
while(temp>0):
    rem=temp%10
    rev=(rev*10)+rem
    temp=temp//10
if rev==num:
    print(f"{rev} is palindrome".format(rev))
else:
    print("{0} is not a palindrome".format(rev))

