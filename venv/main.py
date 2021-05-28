from tkinter import *
from PIL import ImageTk, Image
import cryptography

from Database.ConnectToMySQL import *
from Functions.ViewBooks import *
from Functions.AddBook import *
from Functions.DeleteBook import *
from Functions.UpdateBook import *
from Functions.ViewUsers import *
from Functions.AddUser import *
from Functions.DeleteUser import *
from Functions.UpdateUser import *
from Functions.LendBook import *
from Functions.ViewLent import *
from Functions.ReturnBook import *
from Functions.ViewBorrowers import *
from Functions.ViewBorrowerByName import *
from Functions.ViewBorrowerByBookName import *
from Imgs import *


# tkinter root
root = Tk()

# GUI window
root.title("Library Information Management System - Group 16")
root.geometry("1000x618")
root.wm_attributes('-alpha', 0.9)

# background image
bg_img = Image.open("Imgs/lib_img2.jpg")
[img_width, img_height] = bg_img.size

# resize images while keeping aspect ratio Image.ANTIALIAS
bg_img = bg_img.resize((img_width, img_height), Image.ANTIALIAS)

# import image and turn to tk image
img = ImageTk.PhotoImage(bg_img)

# create canva
cv = Canvas(root)

# add img to canva
cv.create_image(500, 500, image=img)
cv.config(bg="grey", width=img_width, height=img_height)
cv.pack(expand=True, fill=BOTH)

heading_frame = Frame(root, bg="grey", bd=2)
heading_frame.place(relx=0, rely=0, relwidth=1, relheight=0.15)

heading_label = Label(heading_frame, text="G16 Library Information Management System",
                     bg='black', fg='white', font=('Segoe Script', 18))
heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# view_books_icon = PhotoImage(file = r"list.png")
# button1 = Button(root, image=view_books_icon, bg='white', fg='black', command=viewBooks)
button1 = Button(root, text="View All Books", bg='white', fg='black', command=viewBooks)
button1.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.1)

# button2 = Button(root, text="View Authors", bg='white', fg='black')
# button2.place(relx=0.35, rely=0.2, relwidth=0.1, relheight=0.1)
# add_book_icon = PhotoImage(file = r"add-book.png")
# button3 = Button(root, image=add_book_icon, bg='white', fg='black', command=addBook)
button3 = Button(root, text="Add Book", bg='white', fg='black', command=addBook)
button3.place(relx=0.05, rely=0.3, relwidth=0.4, relheight=0.1)


button4 = Button(root, text="Delete Book", bg='white', fg='black', command=deleteBook)
button4.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.1)

button5 = Button(root, text="Update Book", bg='white', fg='black', command=updateBook)
button5.place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.1)

button6 = Button(root, text="View All Users", bg='white', fg='black', command=viewUsers)
button6.place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.1)

button7 = Button(root, text="Add User", bg='white', fg='black', command=addUser)
button7.place(relx=0.55, rely=0.3, relwidth=0.4, relheight=0.1)

button8 = Button(root, text="Delete User", bg='white', fg='black', command=deleteUser)
button8.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.1)

button9 = Button(root, text="Update User", bg='white', fg='black', command=updateUser)
button9.place(relx=0.55, rely=0.5, relwidth=0.4, relheight=0.1)

button10 = Button(root, text="View Lent Book", bg='white', fg='black', command=viewLent)
button10.place(relx=0.05, rely=0.65, relwidth=0.4, relheight=0.1)

button11 = Button(root, text="Lend Book", bg='white', fg='black', command=lendBook)
button11.place(relx=0.05, rely=0.75, relwidth=0.4, relheight=0.1)

button12 = Button(root, text="Return Book", bg='white', fg='black', command=returnBook)
button12.place(relx=0.05, rely=0.85, relwidth=0.4, relheight=0.1)

button13 = Button(root, text="View All Borrowers", bg='white', fg='black', command=viewBorrowers)
button13.place(relx=0.55, rely=0.65, relwidth=0.4, relheight=0.1)

button14 = Button(root, text="View Borrowers By Name", bg='white', fg='black', command=viewBorrowerByName)
button14.place(relx=0.55, rely=0.75, relwidth=0.4, relheight=0.1)

button15 = Button(root, text="View Borrowers By Book Name", bg='white', fg='black', command=viewBorrowersByBookName)
button15.place(relx=0.55, rely=0.85, relwidth=0.4, relheight=0.1)

# initialize GUI
root.mainloop()