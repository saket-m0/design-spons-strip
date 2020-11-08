import cv2

def ResizeImage(image, width):
    image_resized = cv2.resize(image, (width, int(image.shape[0] / image.shape[1] * width)))
    return image_resized

def ShowImage(image):
    cv2.imshow('image', image) 
    k = cv2.waitKey(0) & 0xFF
    
    # wait for ESC key to exit 
    if k == 27:  
        cv2.destroyAllWindows() 

def SaveImage(image, name):
    cv2.imwrite(name,image) 

POSTER = input("Enter Name of the Poster: ")
SPONS_STRIP = input("Enter Name of the Spons Strip: ")

poster = cv2.imread(POSTER)
spons_strip = cv2.imread(SPONS_STRIP)

poster_resized = ResizeImage(poster, 1000)
spons_strip_resized = ResizeImage(spons_strip, 1000)

final = cv2.vconcat([poster_resized, spons_strip_resized])
FINAL_POSTER = input("Enter Name of the Final Poster: ")
SaveImage(final, FINAL_POSTER)
