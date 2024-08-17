num=int(input("Enter the NUmber:"))
count=0
rem=0
sumV=0
temp=he=num
while(temp>0):
    temp=temp//10
    count+=1
while(num>0):
    rem=num%10
    sumV+=rem**count
    num=num//10
if he==sumV:
    print(f"{he} is armstrong Number")
else:
    print(f"{he} is not a armstrong Nuumber")