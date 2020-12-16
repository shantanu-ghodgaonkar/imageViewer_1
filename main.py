from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Tkinter Image Viewer')
root.iconbitmap('S:/Study+Work/Python/TkinterTester/icons/icons8-shark-64.ico')

img1 = ImageTk.PhotoImage(Image.open('C:/Users/shant/Downloads/Album Covers/Dance of Death_Iron Maiden.jpg'))
img2 = ImageTk.PhotoImage(Image.open('C:/Users/shant/Downloads/Album Covers/Innuendo_Queen.jpg'))
img3 = ImageTk.PhotoImage(Image.open('C:/Users/shant/Downloads/Album Covers/2001_Dr DRE.jpg'))
img4 = ImageTk.PhotoImage(Image.open('C:/Users/shant/Downloads/Album Covers/A Day at the Races_Queen.jpg'))
img5 = ImageTk.PhotoImage(Image.open('C:/Users/shant/Downloads/Album Covers/Youthanasia_Megadeth.jpg'))

img_list = [img1, img2, img3, img4, img5]
img_lbl = Label(root, image=img_list[1])
img_lbl.grid(row=0, column=0, columnspan=3)

btn_exit = Button(root, text='EXIT', command=root.quit)
btn_exit.grid(row=1, column=1)
btn_next = Button(root, text='>>')
btn_next.grid(row=1, column=2)
btn_prev = Button(root, text='<<')
btn_prev.grid(row=1, column=0)


if __name__ == '__main__':
    root.mainloop()
