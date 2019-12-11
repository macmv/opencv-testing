import numpy as np
import cv2

cap = cv2.VideoCapture(0)



while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()
  #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  #ret, thres = cv2.threshold(gray, 127,255,cv2.THRESH_BINARY)
  # Our operations on the frame come here
  # this code is for canny edging the blue umbrella I have
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  blue = cv2.inRange(hsv,(90,50,50),(130,255,255))
  blur = cv2.GaussianBlur(blue, (5,5), 0)
  ret, thres = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
  canny = cv2.Canny(thres,100,200)
  contours, hierarchy = cv2.findContours(thres,1,2)
  # create hull array for convex hull points
  hull = []
  # calculate points for each contour
  for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))
  # create an empty black image
  drawing = np.zeros((canny.shape[0], canny.shape[1], 3), np.uint8)
  wMax = 0
  hMax = 0
# draw contours and hull points
  for i in range(len(contours)):
    
    
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    cv2.drawContours(canny, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    x,y,w,h = cv2.boundingRect(hull[i])
    if w > wMax:
      wMax = w
    if h > hMax:
      hMax = h
  img = cv2.rectangle(drawing,(x,y),(x+wMax,y+hMax),(0,255,0),2)
  cv2.imshow('frame', canny)
  cv2.imshow('',img)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

