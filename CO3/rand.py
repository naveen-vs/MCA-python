import random
l1=[1,2,3,4,5,6,7,8,9]
print(random.choice(l1))
print(random.choices(l1,k=4))
print(random.sample(l1,k=1))
random.shuffle(l1)
print(l1)
print(random.randrange(3,9))