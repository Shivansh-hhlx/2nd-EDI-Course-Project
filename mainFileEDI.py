import tkinter as tk
import imageGUI as im
import videoGUI as vi

flag = 3
newI, newV = 0, 0

root1, root2 = 0, 0

root = tk.Tk()

root.title("Dimension Measurement")
root.geometry("600x350")

class mainFileEDI:
    def __init__(self, root):
        self.label1 = tk.Label(root, text = "Choose the option you want", anchor = "w", fg="black", font = "San-serif 15")
        self.label1.pack(fill = tk.X)

        self.gLabel = tk.Label(root,height = 2)
        self.gLabel.pack(fill = tk.X)

        self.eLabel = tk.Label(root, text = "Image measurement", anchor = "w", fg="black", font = "San-serif 14")
        self.eLabel.pack(fill = tk.X)

        self.imageButton = tk.Button(root, text="Image", command=self.Image, fg="Black", font="serif 13", height=3,
                                 width=20)
        self.imageButton.pack(side="top")

        self.gLabel = tk.Label(root, height=2)
        self.gLabel.pack(fill=tk.X)

        self.eLabel = tk.Label(root, text="Video measurement", anchor="w", fg="black", font="San-serif 14")
        self.eLabel.pack(fill=tk.X)

        self.videoButton = tk.Button(root, text="Video", command=self.Video,fg="Black", font="serif 13", height=3,
                                 width=20)
        self.videoButton.pack(side="top")

    def Image(self):
        global root
        global m
        global flag
        global root1
        root1 = tk.Tk()
        root1.title("Dimension Measurement")
        root1.geometry("550x300")
        m = im.imageDimension(root1)
        flag = 0

    def Video(self):
        global root
        global root1
        global m
        global flag
        root2 = tk.Tk()
        root2.title("Dimension Measurement")
        root2.geometry("700x400")
        m = vi.videoDimension(root2)
        flag = 1

if flag == 3:
    m = mainFileEDI(root)

tk.mainloop()