import cv2 as cv

img = cv.imread('Photos/Boston.jpg')
cv.imshow('Dog', img)

#Gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge Cascade
cany = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', cany)

#Dilating the Image
dilated = cv.dilate(cany, (7,7), iterations=1)
cv.imshow('Dilated', dilated)

#eroding
erode = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', erode)

#Resize
resized = cv.resize(img, (700,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

#Cropping
cropped = img[300:500, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
