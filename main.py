from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Tkinter Image Viewer')
root.iconbitmap('S:/Study+Work/Python/TkinterTester/icons/icons8-shark-64.ico')

img1 = ImageTk.PhotoImage(Image.open('S:/Study+Work/Python/TkinterTester/images/IA1.jpg'))
img2 = ImageTk.PhotoImage(Image.open('S:/Study+Work/Python/TkinterTester/images/IA2.jpg'))
img3 = ImageTk.PhotoImage(Image.open('S:/Study+Work/Python/TkinterTester/images/IA3.jpg'))
img4 = ImageTk.PhotoImage(Image.open('S:/Study+Work/Python/TkinterTester/images/IA4.jpg'))
img5 = ImageTk.PhotoImage(Image.open('S:/Study+Work/Python/TkinterTester/images/IA5.jpg'))

img_list = [img1, img2, img3, img4, img5]
btn_exit = Button(root, text='EXIT', command=root.quit)
btn_exit.pack()

if __name__ == '__main__':
    root.mainloop()
