from operator import itemgetter
data = [('abc', 121),('abc', 231),('abc', 148), ('abc',221)]
sorted(data,key=itemgetter(1))