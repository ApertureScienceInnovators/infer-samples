import sys

req_version = (2,5)
cur_version = sys.version_info

if cur_version >= req_version:
   print "success"
else:
   print "Your Python interpreter is too old. Please consider upgrading."