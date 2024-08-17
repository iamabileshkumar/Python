def maxc(a,b):
    return max(a,b)
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
#Method 1
print("max = %d"%maxc(a,b))
#Method 2
if a<b:
    print(f"{b} is greatest".format(b))
else:
    print(f"{a} is smallest".format(a))