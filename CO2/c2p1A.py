def calc_fact(x):
    if x==1:
        return 1
    else:
        return(x* calc_fact(x-1))
n=int(input('number='))
print('the factorial of',n,'is',calc_fact(n))