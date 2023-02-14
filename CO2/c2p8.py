a=[]
n=int(input('Enter the number of items'))
for i in range (0,n):
    s=input('enter the words')
    a.append(s)
temp=a[0]
max1=len(a[0])
for i in a:
    if(len(i)>max1):
        max1=len(i)
        temp=i
print('the longest word is',temp)
print("Lenght of",temp,"is",len(temp))
    