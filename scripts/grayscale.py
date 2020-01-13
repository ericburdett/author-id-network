# grayscale.py

# This script is intended to resize the dataset images to be optimal
# for use on colab and use in pytorch.

import sys
import os
import cv2
import numpy as np

def main(file_path):

    files = os.listdir(file_path)

    count = 0

    for f in files:
        img = cv2.imread(file_path + '/' + f, cv2.IMREAD_GRAYSCALE)
        (thresh, img_grayscale) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        name = f.split('-')[0]

        if not os.path.exists('../../../Datasets/missionaryJournals/grayscale2/' + name):
            os.mkdir('../../../Datasets/missionaryJournals/grayscale2/' + name)
            count = 0

        cv2.imwrite('../../../Datasets/missionaryJournals/grayscale2/' + name + '/' + str(count) + '.jpg', img_grayscale)
        print('Writing ' + name + '-' + str(count))
        count += 1

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args[0])