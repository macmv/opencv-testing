import numpy as np
import cv2

cap = cv2.VideoCapture(0)



while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  # Our operations on the frame come here
 
  blur = cv2.GaussianBlur(gray, (5,5), 0)
  ret, bw = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)
  canny = cv2.Canny(bw,100,200)
  contours, hierarchy = cv2.findContours(bw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  img = cv2.drawContours(frame, contours, -1, (0,255,0), 3)


  cv2.imshow('gray', bw)
  cv2.imshow('edge', canny)
  cv2.imshow('ede', img)

  cv2.imshow('frame', frame)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

