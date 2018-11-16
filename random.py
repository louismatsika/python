import random
#generates a random number
print(random.randint(1,10))

foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))#randomly picks from a list

items = [1, 2, 3, 4, 5]
random.shuffle(items)#shuffels list
print(items)

print(random.sample([1, 2, 3, 4, 5], 3))#picks 3 from a list
