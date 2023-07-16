from tkinter import *
import cv2
import functions

class videoDimension:
    def __init__(self, root):

        self.label1 = Label(root, text = "Choose an image and see the dimensions", anchor = "w", fg = "black", font = "San-serif 15")
        self.label1.pack(fill = X)

        self.gLabel1 = Label(root,height = 2)
        self.gLabel1.pack(fill = X)

        self.eLabel1 = Label(root, text = "Enter side of ArUco", anchor = "w", fg = "black", font = "San-serif 14")
        self.eLabel1.pack(fill = X)

        self.pEntry1 = Entry(root)
        self.pEntry1.pack()

        self.gLabel2 = Label(root, height=2)
        self.gLabel2.pack(fill=X)

        self.eLabel2 = Label(root, text="Enter the camera number", anchor="w", fg="black", font="San-serif 14")
        self.eLabel2.pack(fill=X)

        self.pEntry2 = Entry(root)
        self.pEntry2.pack()

        self.gLabel3 = Label(root,height = 3)
        self.gLabel3.pack(fill = X)

        self.showButton = Button(root, text = "Start&Show", command = self.Command, fg = "Black", font = "serif 13", height = 3, width = 20)
        self.showButton.pack(side = "top")


    def Command(self):
        stringA = self.pEntry1.get()
        intA = float(stringA)

        stringB = self.pEntry2.get()
        intB = int(stringB)
        self.showImg(intA, intB)


    def showImg(self, side, camera):

        capture = cv2.VideoCapture(camera)

        capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

        while True:
            isTrue, frame = capture.read()
            if isTrue:
                pass
            else:
                break

            img, pointsAr = functions.Contours(frame, side)

            cv2.imshow("Camera", img)
            key = cv2.waitKey(1)
            if key == 27:
                break

        capture.release()