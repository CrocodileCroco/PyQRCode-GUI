from tkinter import *
import pyqrcode

root = Tk()

def saveqrcode():
    qrtextget = qrtextentry.get()
    print(qrtextget)
    qrrender = pyqrcode.create(qrtextget)
    filenameget = filenameentry.get()
    print(filenameget)
    qrrender.png(filenameget, scale=10)


title = Label(root, text="PyQRCode GUI")

title.grid(column=0,row=0,columnspan=2)

qrtextlabel = Label(root, text="QR Code Text :")

qrtextentry = Entry(root)

filenamelabel = Label(root, text="Save as :")

filenameentry = Entry(root)

qrtextlabel.grid(column=0, row=1)

qrtextentry.grid(column=1, row=1)

filenamelabel.grid(column=0, row=2)

filenameentry.grid(column=1, row=2)

savebutton = Button(root, text="Save QR Code", command=saveqrcode)

savebutton.grid(column=0, row=3, columnspan=2)

root.mainloop()