fileptr=open("Practise_questions\FileHandling\hello.txt",'a+')
if fileptr:
    print("Open SuccessFully")
try:
    fileptr.write("Hii Everyoneeeeeeee!")
finally:
    fileptr.close()
