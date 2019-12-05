import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
  ret, frame = cap.read()

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  cutoff = cv2.inRange(hsv, (70, 100, 100), (80, 255, 255))
  blur = cv2.GaussianBlur(cutoff, (11, 11), 0)

  contours, h = cv2.findContours(blur, 1, 2)

  for c in contours:
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(frame, [box], 0, (0,255,0), 2)

  cv2.imshow('frame', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()

