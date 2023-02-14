n=int(input('Enter the limit = '))
for i in range(0,n+1):
    for j in range(0,i+1):
        a=i*j
        if a==0:
            continue
        else:
            print(a,end=" ")
    print('\n')
        
    