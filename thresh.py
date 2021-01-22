import cv2 as cv

img = cv.imread('resources/Photos/cats.jpg')
cv.imshow('Cats', img)


cv.waitKey(0)
