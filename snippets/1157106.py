import random, timeit
a = list(range(5)) * 1000
random.shuffle(a)

b = a
print(b is a)


b = [x for x in b if x != 0]
print(b is a)

b.count(0)

a.count(0)


b = a
b = filter(lambda a: a != 2, x)
print(b is a)
