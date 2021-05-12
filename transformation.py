import cv2 as cv
import numpy as np

pic = cv.imread('Photos/boston4.jpg')
img = cv.resize(pic, (700,500), interpolation=cv.INTER_AREA)
cv.imshow('Boston', img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

#Up-Left
translated = translate(img, -100, -100)
cv.imshow('Translated', translated)
#Down-Right
translat = translate(img, 100, 100)
cv.imshow('Translated', translat)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height , width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

#for left rotation +ve point
#for right rotation -ve point ---> rotate(img, -45)
rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# resize
resized= cv.resize(img, (700,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#Flipping
#0 --> flipping the image vertically over the x-axis
#1 --> flip image horizontally over y-axis
#-1 --> flip image both horizontally & vertically
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

#Cropping
cropped = img[100:500, 300:500]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
