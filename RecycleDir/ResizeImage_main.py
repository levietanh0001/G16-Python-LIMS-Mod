from tkinter import *
from PIL import ImageTk, Image
import pymysql
from tkinter import messagebox

from ViewBooks import *
from AddBook import *
from DeleteBook import *
from UpdateBook import *

from ViewUsers import *
from AddUser import *
from DeleteUser import *
from UpdateUser import *

from LendBook import *
from ReturnBook import *

import cryptography
import mysql.connector

# database details
my_pass = "123321"
my_db = "g16_db"

# connect to database
con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_db, port=3306)
cur = con.cursor()

# tkinter root
root = Tk()
root.state('zoomed')

# GUI window
root.title("Library Information Management System - Group 16")
root.geometry("1000x618")

# [img_width, img_height] = bg_img.size
#
#     # resize images while keeping aspect ratio Image.ANTIALIAS
# bg_img = bg_img.resize((img_width,img_height), Image.ANTIALIAS)
#
#     # import image and turn to tk image
# img = ImageTk.PhotoImage(bg_img)

bg = PhotoImage("./lib_img.jpg")
# create canva
cv = Canvas(root, width=1000, height=618)
cv.pack(fill=BOTH, expand=True)
cv.create_image(0, 0, image=bg, anchor="nw")

# add img to canva
# cv.create_image(500, 500, image = new_bg)
# # cv.config(bg="grey",width=img_width, height=img_height)
# cv.pack(expand=True, fill=BOTH)


heading1 = Frame(root, bg="grey", bd=0.3)
heading1.place(relx=0, rely=0, relwidth=1, relheight=0.15)

headingLabel = Label(heading1, text="G16 Library Information Management System",
                     bg='black', fg='white', font=('Georgia', 18))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

button1 = Button(root, text="View All Books", bg='black', fg='white', command=viewBooks)
button1.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.1)

button2 = Button(root, text="Add Book", bg='black', fg='white', command=addBook)
button2.place(relx=0.05, rely=0.3, relwidth=0.4, relheight=0.1)

button3 = Button(root, text="Delete Book", bg='black', fg='white', command=deleteBook)
button3.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.1)

button4 = Button(root, text="Update Book", bg='black', fg='white', command=updateBook)
button4.place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.1)

button5 = Button(root, text="View All Users", bg='black', fg='white', command=viewUsers)
button5.place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.1)

button6 = Button(root, text="Add User", bg='black', fg='white', command=addUser)
button6.place(relx=0.55, rely=0.3, relwidth=0.4, relheight=0.1)

button7 = Button(root, text="Delete User", bg='black', fg='white', command=deleteUser)
button7.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.1)

button8 = Button(root, text="Update User", bg='black', fg='white', command=updateUser)
button8.place(relx=0.55, rely=0.5, relwidth=0.4, relheight=0.1)

button9 = Button(root, text="Lend Book", bg='black', fg='white', command=lendBook)
button9.place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.1)

button10 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
button10.place(relx=0.28, rely=0.75, relwidth=0.45, relheight=0.1)


def resizer(e):
    # global bg_img, resized_bg, new_bg
    bg_img = Image.open("lib_img.jpg")
    resized_bg = bg_img.resize((e.width, e.height), Image.ANTIALIAS)
    new_bg = ImageTk.PhotoImage(resized_bg)
    cv.create_image(0, 0, image=new_bg, anchor="nw")


root.bind('<Configure>', resizer)
# initialize GUI
root.mainloop()
