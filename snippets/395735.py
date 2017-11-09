import inspect
class X(object):
    pass

inspect.isclass(X)


x = X()
isinstance(x, X)

y = 25
isinstance(y, X)
