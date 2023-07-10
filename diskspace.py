#-------------python script to check disk space-----------
import os
import shutil
print(os.getcwd())

total,used,free = shutil.disk_usage("/")
print(f"The total disk space is: {total // (2**30)} GB")
print(f"The used disk space is: {used // (2**30)} GB")
print(f"The free disk space is: {free // (2**30)} GB")