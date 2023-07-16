import cv2
import numpy as np

id = 1

arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_7X7_1000)

tag_size = 1000

tag = np.zeros((tag_size, tag_size, 1), dtype="uint8")
cv2.aruco.drawMarker(arucoDict, id, tag_size, tag, 1)

tag_name = "arucoMarkers/DICT_7X7_1000_" + str(id) + ".png"

cv2.imwrite(tag_name, tag)
cv2.imshow("Aruco Tag", tag)


cv2.waitKey(0)

cv2.destroyAllWindows()