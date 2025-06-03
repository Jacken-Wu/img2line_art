import cv2
import numpy as np
import os
import sys

line_width = 5
filter_size = 7
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    arg1 = int(sys.argv[1])
    arg1 = arg1 if arg1 >= 3 else 3
    arg1 = arg1 if arg1 % 2 == 1 else arg1 + 1
    line_width = arg1
if len(sys.argv) > 2:
    filter_size = int(sys.argv[2])


def get_files():
    files = list(filter(lambda x: x in ['input.jpg', 'input.png', 'input.jpeg'], os.listdir()))
    return files


def edge(filename, blockSize=5, C=7):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    img_edge = cv2.adaptiveThreshold(img, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY,
                                     blockSize=blockSize,
                                     C=C)

    cv2.imwrite('output_edge.png', img_edge)

    # imgs = np.hstack([img, img_edge])

    # screen_max_width = 1920 - 100
    # screen_max_height = 1080 - 100
    # if imgs.shape[1] > screen_max_width:
    #     imgs = cv2.resize(imgs, (screen_max_width, int(imgs.shape[0] * screen_max_width / imgs.shape[1])))
    # if imgs.shape[0] > screen_max_height:
    #     imgs = cv2.resize(imgs, (int(imgs.shape[1] * screen_max_height / imgs.shape[0]), screen_max_height))

    # cv2.imshow('Images', imgs)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    files = get_files()
    if len(files) == 0:
        print('No input image found.')
    else:
        edge(files[0], blockSize=line_width, C=filter_size)
