import collections

def split(inp):
    b=[]
    a=''
    for i in inp:
        if i not in b:
            b.append(i)
            a=''
        else:
            a=''
        if a:
            b.append(i)
    return b
inp='aabccdaa'
arr=split(inp)
a=[]
for i in arr:
    a.append(inp.count(i))
print(f"the Maximum Count of letter is {max(a)}")
#method 2 Using Counter in Collections
ou=collections.Counter('aabccdaa')
ou=ou.most_common()[0]
print(ou)