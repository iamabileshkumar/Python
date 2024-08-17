#Words Frequency in String Shorthands
test_str = 'Gfg is best is'
test_str=test_str.split()
new={}
for i in test_str:
    new[i]= test_str.count(i)
print(new)