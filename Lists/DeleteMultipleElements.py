arr=[12, 15, 3, 10, 9,3]
a=[3,15]
#Method1
out=[]
for i in arr:
    if i not in a:
        out.append(i)
print(out)
#Method2
arr=[i for i in arr if i not in a]
print(arr)
