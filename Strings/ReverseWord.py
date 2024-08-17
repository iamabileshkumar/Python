str="Hello i am Abilesh"
tup=[]
b=''
for i in str:
    if i==" ":
        tup.append(b)
        b=''
    else:
        b+=i
if b:
    tup.append(b)
for j in range(len(tup)-1,-1,-1):
    print(tup[j],end=" ")
