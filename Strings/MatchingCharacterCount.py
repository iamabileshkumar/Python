str1 = 'aabcddekll12@'
str2 = 'bb2211@55k'
str4=[]
str1=set(str1)
str2=set(str2)
str3=len(str1.intersection(str2))
print(f'Count of Matching Character by method 1 is {str3}')
#Method 2
for i in str1:
    if i in str2:
        str4.append(i)
print(f'Count of Matching Character by method 2 is {len(str4)}')