import math
n=int(input('Enter the number :'))
print('The factors of ',n,'are ',end=" ")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")