from tkinter import *
from PIL import ImageTk, Image
import cryptography

from ViewBooks import *
# from ViewBooks2 import *
from AddBook import *
from DeleteBook import *
from UpdateBook import *

from ViewUsers import *
from AddUser import *
from DeleteUser import *
from UpdateUser import *

from LendBook import *
from ViewLent import *
from ReturnBook import *

def show_frame(frame):
    frame.tkraise()
def show_view_books(view_books_frame):
    # show_frame(view_books_frame)
    # viewBooks2(view_books_frame)
    show_frame(view_books_frame)

# cho frame to len o ban sample

# tkinter root
root = Tk()

# GUI window
root.title("Library Information Management System - Group 16")
root.geometry("1000x618")

# background image
bg_img = Image.open("lib_img2.jpg")
[img_width, img_height] = bg_img.size

# resize images while keeping aspect ratio Image.ANTIALIAS
bg_img = bg_img.resize((img_width, img_height), Image.ANTIALIAS)

# import image and turn to tk image
img = ImageTk.PhotoImage(bg_img)

main_frame = Frame(root, bg="grey")
# main_frame.grid(row=0, column=0, sticky='nsew')
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

view_books_frame = Frame(root, bg='blue')
# view_books_frame.grid(row=0, column=0, sticky='nsew')
view_books_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
view_books_frame = tk.Label(view_books_frame, bg='green', text='This is view books window')
view_books_frame.pack()



# create canva
cv = Canvas(main_frame)

# add img to canva
cv.create_image(500, 500, image=img)
cv.config(bg="black", width=img_width, height=img_height)
cv.pack(expand=True, fill=BOTH)

heading_label = Label(main_frame, text="G16 Library Information Management System",
                     bg='black', fg='white', font=('Segoe Script', 18))
heading_label.place(relx=0, rely=0, relwidth=1, relheight=0.1)

button1 = Button(main_frame, text="View All Books", bg='white', fg='black', command=lambda:show_frame(view_books_frame))
button1.place(relx=0.05, rely=0.2, relwidth=0.4, relheight=0.1)

# button2 = Button(root, text="View Authors", bg='white', fg='black')
# button2.place(relx=0.35, rely=0.2, relwidth=0.1, relheight=0.1)

button3 = Button(main_frame, text="Add Book", bg='white', fg='black', command=addBook)
button3.place(relx=0.05, rely=0.3, relwidth=0.4, relheight=0.1)

button4 = Button(main_frame, text="Delete Book", bg='white', fg='black', command=deleteBook)
button4.place(relx=0.05, rely=0.4, relwidth=0.4, relheight=0.1)

button5 = Button(main_frame, text="Update Book", bg='white', fg='black', command=updateBook)
button5.place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.1)

button6 = Button(main_frame, text="View All Users", bg='white', fg='black', command=viewUsers)
button6.place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.1)

button7 = Button(main_frame, text="Add User", bg='white', fg='black', command=addUser)
button7.place(relx=0.55, rely=0.3, relwidth=0.4, relheight=0.1)

button8 = Button(main_frame, text="Delete User", bg='white', fg='black', command=deleteUser)
button8.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.1)

button9 = Button(main_frame, text="Update User", bg='white', fg='black', command=updateUser)
button9.place(relx=0.55, rely=0.5, relwidth=0.4, relheight=0.1)

button10 = Button(main_frame, text="View Lent Book", bg='white', fg='black', command=viewLent)
button10.place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.1)

button11 = Button(main_frame, text="Lend Book", bg='white', fg='black', command=lendBook)
button11.place(relx=0.28, rely=0.75, relwidth=0.45, relheight=0.1)

button12 = Button(main_frame, text="Return Book", bg='white', fg='black', command=returnBook)
button12.place(relx=0.28, rely=0.85, relwidth=0.45, relheight=0.1)

show_frame(main_frame)
# initialize GUI
root.mainloop()