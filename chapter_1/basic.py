import cv2 as cv

img = cv.imread('resources/Photos/cat.jpg')

cv.imshow('Cat', img)

# Converting img to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the images
dilated = cv.dilate(canny, (7, 7), iterations=1)
cv.imshow('Dilated', dilated)

# Eroding
erode = cv.erode(dilated, (7, 7), iterations=1)
cv.imshow('Eroding', erode)

# Resize
resize = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resize)

# Cropping
cropped = img[100:200, 200:400]
cv.imshow('Cropping', cropped)

cv.waitKey(0)
