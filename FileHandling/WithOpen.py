with open("Practise_questions\FileHandling\WithOpen.txt",'w') as f:
    a=['hello\n','I am\n','Writing Code']
    f.writelines(a)
    f.close()
fileptr=open("Practise_questions\FileHandling\WithOpen.txt",'r')
c=fileptr.read()
print(c)