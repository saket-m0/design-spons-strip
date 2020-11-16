import cv2
import os


def makeFileName(file):
    filename = file[:-4] + ' final.png'
    return filename

def attachSponsStrip(array):
    spons_strip_1 = cv2.imread('Assets/SponsStrips/spons-strip-1.png')
    spons_strip_2 = cv2.imread('Assets/SponsStrips/spons-strip-2.png')

    for i, file in enumerate(array):
        poster = cv2.imread('Assets/' + file)
        
        if (i % 2 == 0):
            final = cv2.vconcat([ResizeImage(poster, 1000), ResizeImage(spons_strip_2, 1000)])
        else:
            final = cv2.vconcat([ResizeImage(poster, 1000), ResizeImage(spons_strip_1, 1000)])

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


posters = []
for file in os.listdir('Assets/'):
    if file.endswith('.png'):
        posters.append(file)

attachSponsStrip(posters)
