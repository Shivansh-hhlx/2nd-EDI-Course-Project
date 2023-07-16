from tkinter import *
from tkinter import filedialog
import cv2
import functions

class imageDimension:
    def __init__(self, root):

        self.label1 = Label(root, text = "Choose an image and see the dimensions", anchor = "w", fg = "black", font = "San-serif 15")
        self.label1.pack(fill = X)

        self.gLabel = Label(root,height = 2)
        self.gLabel.pack(fill = X)

        self.eLabel = Label(root, text = "Enter side of ArUco", anchor = "w", fg = "black", font = "San-serif 14")
        self.eLabel.pack(fill = X)

        self.pEntry = Entry(root)
        self.pEntry.pack()

        self.gLabel1 = Label(root,height = 3)
        self.gLabel1.pack(fill = X)

        self.showButton = Button(root, text = "Open&Show", command = self.Command, fg = "Black", font = "serif 13", height = 3, width = 20)
        self.showButton.pack(side = "top")

    def Command(self):
        stringA = self.pEntry.get()
        intA = float(stringA)
        self.showImg(intA)


    def showImg(self, side):
        imgPath = filedialog.askopenfilename(initialdir = "C:/Users/Admin/Desktop", filetypes = [("Image File", "*.png; *.jpg; *.jpeg")])

        img = cv2.imread(imgPath)

        img, pointsAr = functions.Contours(img, side)

        img = cv2.resize(img, (0, 0), None, 0.5, 0.5)
        cv2.imshow("Camera", img)
        cv2.waitKey(0)