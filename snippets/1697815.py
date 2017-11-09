import time
from time import mktime
from datetime import datetime

struct = time.localtime()

dt = datetime.fromtimestamp(mktime(struct))
print dt