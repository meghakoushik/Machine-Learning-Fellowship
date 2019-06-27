#program to get the effective group id, effective user id, real group id, a list of supplemental group ids.

import os

print("Effective group id:", os.getegid())
print("Effective User id:", os.geteuid())
print("real group id:", os.getgid())
print("list of supplemetal group id:", os.getgroups())