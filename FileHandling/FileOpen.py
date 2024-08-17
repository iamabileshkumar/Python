fileptr=open("C:\Abi\Education\Data Analysis\Python\Jupyter Notebook\Practise_questions\FileHandling\hello.txt",'a+')
if fileptr:
    print("Open SuccessFully")
try:
    fileptr.write("Hii Everyoneeeeeeee!")
finally:
    fileptr.close()