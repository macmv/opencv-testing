#this code will only work when the paper is parrell to the camera lens, 
#so I still need to work on it
#It shows the vertical distance 
#and horizontal shift of the camera and the paper

import cv2
import numpy as np

# turn on camera at port 1
cap = cv2.VideoCapture(1)
# width of the paper in inches 
# this number should be the same as the actual paper width 
KNOWN_WIDTH = 5.5

#the focallength of the camera will need to be modified
#It is currently defaulted to my camera
#this number will vary due to different camera modules 

#laptop focallength 
#focalLength = 800
#webCam focallength
focalLength = 1200



def distance_to_camera(knownWidth, focalLength, perWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / perWidth

while(True):
	# read frame from camera
	ret, frame = cap.read()
  #grayscale it and blur it and edge it
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)

	# find the contours in the edged frame and keep the largest one;
	# we'll assume that this is our piece of paper in the frame
	contours, h = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	# find all contours
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

	#get the max countor detail
	x,y,w,h	= cv2.boundingRect(max_box)
	#get image width
	imageW = frame.shape[1]
  	#vertical distance
	distanceV = 0
	#horizontal Shift
	distanceH = 0
	# only draw the contour and calculate distance once the max_area has been set
	if max_area > -1:
		cv2.drawContours(frame, [max_box], 0, (0,255,0), 2)
		#this is the instant distance between paper and camera
		distanceV = distance_to_camera(KNOWN_WIDTH, focalLength, w)
		#default means when camera is at the origin of the paper
		default_W = (KNOWN_WIDTH * focalLength) / distanceV
		default_Shift = (imageW / 2) - (default_W / 2)
		#this is the instant distance of horizontal shift
		distanceH = (default_Shift - x) / focalLength * distanceV
    

    #show distance
	cv2.putText(frame, "%.2fft" % (distanceV / 12),
		(frame.shape[1] - 200, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
		2.0, (0, 255, 0), 3)
	cv2.putText(frame, "%.2fin" % distanceH,
		(frame.shape[1] - 200, frame.shape[0] - 80), cv2.FONT_HERSHEY_SIMPLEX,
		2.0, (0, 255, 0), 3)

	# draw frame to screen
	cv2.imshow('frame', frame)
	cv2.imshow("edge", edged)
	# if q is pressed, quit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# close windows
cap.release()
cv2.destroyAllWindows()
