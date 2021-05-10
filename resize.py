import cv2 as cv

def rescaleFrame(frame, scale=0.15):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
def changeRes(width, height):
    #Live video not for images like facecam

    capture.set(3, width)
    capture.set(4, height)

capture = cv.VideoCapture('Videos/dogs.mp4')
while True:
     isTrue, frame = capture.read()
     frame_resized = rescaleFrame(frame)
     cv.imshow('Video', frame)
     cv.imshow('Video Resized', frame_resized)

     if cv.waitKey(20) & 0xFF == ord('d'):
         break
 capture.release()
 cv.destroyAllWindows()
 cv.waitKey(0)
img = cv.imread('Photos/cat.jpg')
resize_image = rescaleFrame(img)
cv.imshow('Cat', resize_image)


cv.waitKey(0)
