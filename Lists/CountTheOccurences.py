arr=[12,3,4,54,5,5,6,6,1,22,33,33,12]
count=0
key=int(input("Enter the Number to Find the Occurences"))
#Method1
for k,v in enumerate(arr):
    if key==arr[k]:
        count+=1
print(count)

#Method2
import collections
arr=collections.Counter(arr)
print(arr[key])
