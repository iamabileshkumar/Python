inp='geeks for geeks'
var='geek'
for i in inp:
    if var[0]==i:
        if inp[i.index(i):i.index(i)+len(var)]==var:
            print("yes")
        else:
            print("no")
