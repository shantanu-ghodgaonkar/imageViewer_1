from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Tkinter Image Viewer')
root.iconbitmap('S:/Study+Work/Python/TkinterTester/icons/icons8-shark-64.ico')

btn_exit = Button(root, text='EXIT', command=root.quit)
btn_exit.pack()

if __name__ == '__main__':
    root.mainloop()