from collections import defaultdict

d = defaultdict(lambda: 0)

for i in xrange(100):
    d[i % 10] += 1
