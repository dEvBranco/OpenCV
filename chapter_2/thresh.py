import cv2 as cv

img = cv.imread('resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding
treshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('SImple Threshold', thresh)

treshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('SImple Threshold Inverse', thresh_inv)

# Adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 13, 1) # noqa
cv.imshow('Adaptive Threshold', adaptive_thresh)


cv.waitKey(0)
