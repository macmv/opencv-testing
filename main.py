import cv2
import numpy as np

# turn on camera at port 0
cap = cv2.VideoCapture(0)

while(True):
  # read image from camera
  ret, frame = cap.read()

  # convert to hsv
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  # find only green colors
  cutoff = cv2.inRange(hsv, (70, 90, 90), (90, 256, 256))
  # blur image
  blur = cv2.GaussianBlur(cutoff, (11, 11), 0)
  # darken, to remove small areas the blur didn't remove
  darken = cv2.add(blur, np.array([-50.0]))

  # find all contours
  contours, h = cv2.findContours(darken, 1, 2)

  max_area = -1
  max_box = None
  # loop through contours
  for c in contours:
    # rect is ((x, y), (w, h), rot)
    rect = cv2.minAreaRect(c)
    # gets the four points on the outside of the rectangle
    box = cv2.boxPoints(rect)
    # convert to int
    box = np.int0(box)
    # find area of contour
    area = cv2.contourArea(box)
    # if area is greater than max, set the max area and contour
    if area > max_area:
      max_area = area
      max_box = box

  # only draw the contour of the max_area has been set
  if max_area > -1:
    cv2.drawContours(frame, [max_box], 0, (0,255,0), 2)

  # draw image to screen
  cv2.imshow('frame', frame)

  # if q is pressed, quit
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# close windows
cap.release()
cv2.destroyAllWindows()

