import numpy as np
import cv2

frame = cv2.imread('none.jpg')


canny = cv2.Canny(frame,100,200)
contours, hierarchy = cv2.findContours(canny,1,2)
# create hull array for convex hull points
hull = []
# calculate points for each contour
for i in range(len(contours)):
  # creating convex hull object for each contour
  hull.append(cv2.convexHull(contours[i], False))
  # create an empty black image
  drawing = np.zeros((canny.shape[0], canny.shape[1], 3), np.uint8)

# draw contours and hull points
for i in range(len(contours)):
  color_contours = (0, 255, 0) # green - color for contours
  color = (255, 0, 0) # blue - color for convex hull
# draw ith contour
  cv2.drawContours(canny, contours, i, color_contours, 1, 8, hierarchy)
# draw ith convex hull object
  rect = cv2.minAreaRect(hull[i])
  box = cv2.boxPoints(rect)
  box = np.int0(box)
  im = cv2.drawContours(drawing,[box],0,(0,0,255),2)
cv2.imshow('frame', canny)
cv2.imshow('',im)
print(hull)
cv2.waitKey(0)
cv2.destroyAllWindows()

