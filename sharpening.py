import cv2
import numpy as np
import os
images_input_dir = 'image_input/'
images_output_dir = 'image_output/'


def sharpening(img, k = 2):
    coarse = cv2.bilateralFilter(img, 18, 150, 150)
    fine = img - coarse
    out = img + k * fine
    return out


def view_image(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    for file in os.listdir(images_input_dir):
        image = cv2.imread(os.path.join(images_input_dir, file))
        output = sharpening(image)
        cv2.imwrite(os.path.join(images_output_dir, '{}_output.jpg'.format(file)), output)
        print ('{} sharpened'.format(file))


if __name__ == '__main__':
    main()
