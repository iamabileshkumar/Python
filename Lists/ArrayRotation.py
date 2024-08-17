arr=[1,8,88,4,5]
rot=[0,0,0,0,0]
key=int(input("Enter the Key:"))
for i in range(len(arr)):
    rot[i-key]=arr[i]
print(rot)