import copy
dict1={'a': 1, 'b': {'m': 4, 'n': 5, 'o': 6}, 'c': 3}
dict2 = copy.deepcopy(dict1)
print dict2