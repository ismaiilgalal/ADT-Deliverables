##### I tried passing a screenshot of the schematic to an OCR tool, it couldn't get any of the labels on the drawing.########
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2
import numpy as np
from matplotlib import pyplot as plt

# def get_grayscale(image):
#     return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#
# # thresholding
# def thresholding(image):
#     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text


# img = cv2.imread('blue text.png')


# dst = cv2.fastNlMeansDenoising(img, None, 10, 10, 7, 21)
# plt.subplot(121),plt.imshow(img)
# plt.subplot(122),plt.imshow(dst)
# plt.show()
#
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# # define range of blue color in HSV
# lower_blue = np.array([110, 50, 50])
# upper_blue = np.array([130, 255, 255])
#
# # Threshold the HSV image to get only blue colors
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
#
# # Bitwise-AND mask and original image
# res = cv2.bitwise_and(img, img, mask=mask)
#
# cv2.imshow('image', img)
# cv2.imshow('mask', mask)
# cv2.imshow('res', res)
# k = cv2.waitKey(5) & 0xFF
# # if k == 27:
# #     break
# cv2.imwrite('mask.png', mask)
# cv2.waitKey()
#
# cv2.destroyAllWindows()



# thresh = thresholding(img)

# cv2.imshow('img', thresh)

# cv2.waitKey(0)

#
#
print(ocr_core('zoom.png'))


