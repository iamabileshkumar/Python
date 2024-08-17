input='Geeks123For123Geeks'
for i in input:
    if i.isdigit():
        input=input.replace(i,'',1)
print(input.strip())
