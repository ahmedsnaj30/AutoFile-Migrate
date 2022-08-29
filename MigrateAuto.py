import os
import sys
import shutil
import argparse

# command(1): python3 MigrateAuto.py <Target file>

# file named End-patching-linux-input_1.txt
source = str(sys.argv[1])

allfiles = os.listdir(source)

for file in allfiles:
    dest = file.replace("-", "/")

    # Extracts pathway from destination name
    path = dest.rsplit("/",1)[0] + '/'
    print(path)

    # Creates directories if path doesn't exist
    if not os.path.isdir(path):
        os.makedirs(path)
        print("Created path: ", path)
    else:
        print(path, "already exists")

    shutil.move(source + file, dest)
    # shutil.copyfile(source + file, dest) 