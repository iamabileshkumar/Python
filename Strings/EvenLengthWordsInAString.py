#Python program to print even length words in a string
s = "i am Mick" 
s=s.split()
for i in s:
    if len(i)%2==0:
        print(i,end=" ")