import numpy as np
import cv2 as cv

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)


#1 Point the image a cetain colour
blank[100:200, 200:300] = 0,0,255
cv.imshow('Red', blank)

#2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# #3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blank)

# #4. Draw a Line
cv.line(blank, (100,250), (300, 250), (255,255,255), thickness=3)
cv.imshow('Line', blank)

#5. Write Text
# If the text length is greater than the window than by changing the coordinate we can show the text
cv.putText(blank, 'Hello',(250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255,0),2)
cv.imshow('Text', blank)
cv.waitKey(0)