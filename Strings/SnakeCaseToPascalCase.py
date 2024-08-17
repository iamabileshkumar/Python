#Convert Snake case to Pascal case
inp='geeks_for_geeks'
inp=inp.split("_")
for i in range(len(inp)):
    inp[i]=inp[i].capitalize()
inp=''.join(inp)
print(inp)