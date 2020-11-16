import cv2
import os
import random


def makeFileName(file):
    filename = file[:-4] + ' final.png'
    return filename


def attachSponsStrip(posters, spons_strips):
    for i, file in enumerate(posters):
        poster = cv2.imread('Assets/' + file)
        spons_strip = cv2.imread('Assets/SponsStrips/' + random.choice(spons_strips))
        final = cv2.vconcat([ResizeImage(poster, 1000), ResizeImage(spons_strip, 1000)])

        SaveImage(final, makeFileName(file))


def ResizeImage(image, width):
    height = int(image.shape[0] / image.shape[1] * width)
    image_resized = cv2.resize(image, (width, height))
    return image_resized


def ShowImage(image):
    cv2.imshow('image', image)
    k = cv2.waitKey(0) & 0xFF

    # wait for ESC key to exit
    if k == 27: 
        cv2.destroyAllWindows()


def SaveImage(image, name):
    cv2.imwrite('Final/' + name, image)


def scanFolder(path):
    array = []
    for file in os.listdir(path):
        if file.endswith('.png'):
            array.append(file)

    return array

posters = scanFolder('Assets/')
spons_strips = scanFolder('Assets/SponsStrips/')
attachSponsStrip(posters, spons_strips)
