# data.py

# This file is for manipulating the missionary journal dataset to work with our author-id-network
# The script to produce this file is shown below...

import sys
import os
import string
from lxml import etree

def directory(file_path):
    files = os.listdir(path=file_path)

    for f in files:
        move_missionary(file_path + '/' + f)

def rename_missionary(file_path):
    dir_name = None
    missionary_name = None

    files = os.listdir(path=file_path)

    count = 0

    for f in files:
        if f.startswith('REP'):
            dir_name = f
        if f.endswith('.xml'):
            tree = etree.parse(file_path + '/' + f).getroot()
            missionary_name = tree[0][0][0][0][0].text

    missionary_name = missionary_name.translate(str.maketrans('', '', string.punctuation))
    missionary_name = missionary_name.translate(str.maketrans('', '', string.digits))
    missionary_name = missionary_name.strip()
    missionary_name = missionary_name.replace(' ', '_')
    local_dir = file_path + '/' + dir_name
    
    jpgs = os.listdir(local_dir)
    for jpg in jpgs:
        prev_name = local_dir + '/' + jpg
        new_name = local_dir + '/' +  missionary_name + '-' + str(count) + '.jpg'
        os.rename(prev_name, new_name)
        count += 1
        print(prev_name, new_name)


def move_missionary(file_path):
    count = 1
    dir_name = None

    files = os.listdir(path=file_path)

    for f in files:
        if f.startswith('REP'):
            dir_name = f

    local_dir = file_path + '/' + dir_name

    jpgs = os.listdir(local_dir)
    for jpg in jpgs:
        old_dir = local_dir + '/' + jpg
        new_dir = local_dir + '/../../../data/' + jpg

        while (os.path.exists(new_dir)):
            new_dir = new_dir[:-4]
            new_dir = new_dir + '-' + str(count) + '.jpg'
            count += 1

        print('Moving ', old_dir, ' to ', new_dir)
        os.rename(old_dir, new_dir)


def main(args):
    print(args)
    if len(args) != 1:
        print("Must specify a path")
    else:
        directory(args[0])


if __name__ == "__main__":
    main(sys.argv[1:])