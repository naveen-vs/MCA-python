a=int(input('Enter current year :'))
b=int(input('enter the final year :'))
if a<b:
    for i in range(a,b):
        if i%4==0 and i%100!=0 or i%400==0 and i%100==0:
            print('the leap year is ',i)
else:
    print('final year must be greater than current year')
