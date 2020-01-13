# dictionary.py

# This script is used for the purpose of creating a dictionary of outputs for
# author classification

import os
import sys

def main(file_path):

    files = os.listdir(file_path)

    dictionary = {}
    count = 0

    for f in files:
        name = f.split('-')[0]

        if name not in dictionary:
            dictionary[name] = count
            count += 1

    print(dictionary)



if __name__ == "__main__":
    main(sys.argv[1])