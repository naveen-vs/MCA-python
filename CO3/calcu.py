import CALCULATOR
a=int(input('enter the number a= '))
b=int(input('enter the number b= '))
n=int(input('enter the operation to perform 1.Addition 2.substracton 3.multiplication 4.division   :'))
if n==1:
    s1=CALCULATOR.sum(a,b)
    print(s1)
elif n==2:
    s2=CALCULATOR.sub(a,b)
    print(s2)
elif n==3:
    s3=CALCULATOR.mult(a,b)
    print(s3)
elif n==4:
    s4=CALCULATOR.div(a,b)
    print(s4)
else:
    print('entered number is incorrect')
