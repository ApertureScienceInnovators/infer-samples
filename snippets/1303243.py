import six

obj = ' test please ignore ' # modified

if isinstance(obj, six.string_types):
    print('obj is a string!')