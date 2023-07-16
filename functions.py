import cv2
import numpy as np
import math

def getContours(img, imgContour, side):

    parameters = cv2.aruco.DetectorParameters_create()
    aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_1000)

    corners, _, _ = cv2.aruco.detectMarkers(imgContour, aruco_dict, parameters=parameters)

    if corners == []:
        return imgContour, 0

    arucoPerimeter = cv2.arcLength(corners[0], True)

    arucoSide = arucoPerimeter / 4

    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    pointAr = []

    for con in contours:
        area = cv2.contourArea(con)
        if area > 2000:
            cv2.drawContours(imgContour, con, -1, (255, 0, 255), 3)
            peri = cv2.arcLength(con, True)
            approx = cv2.approxPolyDP(con, 0.02 * peri, True)
            rect = cv2.minAreaRect(approx)
            (x, y), (w, h), _ = rect
            cv2.circle(imgContour, (int(x), int(y)), 5, (0, 0, 255), -1)

            x1, y1, w1, h1 = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 3)

            w = w / arucoSide
            h = h / arucoSide

            w = w * side
            h = h * side

            cv2.putText(imgContour, "Width {}".format((w)), (int(x - 50), int(y - 20)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (100, 200, 0), 2)
            cv2.putText(imgContour, "Height {}".format((h)), (int(x - 50), int(y + 20)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (100, 200, 0), 2)

            pointAr.append(approx)

    return imgContour, pointAr

def Contours(img, side):
    imgContour = img.copy()
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

    imgCanny = cv2.Canny(imgGray, 120, 120)

    kernel = np.ones((5, 5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations = 1)

    #imgz = cv2.resize(imgDial, (0, 0), None, 0.5, 0.5)
    #cv2.imshow("Canny", imgz)

    return getContours(imgDial, imgContour, side)