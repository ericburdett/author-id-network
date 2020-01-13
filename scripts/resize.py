# resize.py

# This script is intended to resize the dataset images to be optimal
# for use on colab and use in pytorch.

import sys
import os
import cv2
import numpy as np

START_HEIGHT = 125 # FROM TOP
START_WIDTH = 125 # FROM LEFT

IMG_HEIGHT = 256
IMG_WIDTH = 256

def main(file_path):

    files = os.listdir(file_path)

    for f in files:
        img = cv2.imread(file_path + '/' + f)
        img = img[START_HEIGHT:START_HEIGHT+IMG_HEIGHT, START_WIDTH:START_WIDTH+IMG_WIDTH]
        cv2.imwrite('../../../Datasets/missionaryJournals/resized/' + f, img)
        print('Writing ' + f)

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args[0])