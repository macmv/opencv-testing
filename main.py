
import cv2

cap = cv2.VideoCapture(0)

while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()

  # Our operations on the frame come here
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  cutoff = cv2.inRange(hsv, (70, 50, 50), (80, 256, 256))

  # Display the resulting frame
  cv2.imshow('frame', cutoff)

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

