from operator import length_hint
arr=[1,2,4,8,45,5,17,1,2,2,77]
print(length_hint(arr))
#method 2
print(len(arr))
#method 3
c=0
for i in arr:
    c+=1
print(c)