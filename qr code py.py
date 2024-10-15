from tkinter import *
import pyqrcode
import png
from pyqrcode import QRCode
root=Tk()
root.maxsize(600,600)
def f1():
    text=s.get()
    qrcode=pyqrcode.create(text)
    file='myqr.png'
    qrcode.png(file,scale=8)
s=StringVar()
Label(root,text="qr genrator", font='algerian 22').place(x=167,y=0)
Label(root,text="enter your text or url", font='aerial 12').place(x=1,y=40)
Entry(root,textvariable=s).place(x=1,y=70)
Button(root,text='generate',font='aerial 13',command=f1).place(x=7,y=100)
root.mainloop()
