from tkinter import *
# from tkinter.ttk import *
from PIL import ImageTk, Image
import cryptography
import io

from Database.ConnectToMySQL import *
# from Functions.ViewBooks import *
from Functions.ViewBooksDraft import *
# from Functions.AddBook import *
from Functions.AddBookDraft import *
# from Functions.DeleteBook import *
from Functions.DeleteBookDraft import *
# from Functions.UpdateBook import *
from Functions.UpdateBookDraft import *
from Functions.ViewUsersDraft import *
from Functions.AddUserDraft import *
from Functions.DeleteUserDraft import *
from Functions.UpdateUserDraft import *
from Functions.LendBook import *
from Functions.ViewLent import *
from Functions.ReturnBook import *
from Functions.ViewBorrowers import *
from Functions.ViewBorrowerByName import *
from Functions.ViewBorrowerByBookName import *
from Imgs import *

def show_frame_main(frame):
    frame.tkraise()
def show_frame_add_book(frame_add_book):
    addBook(frame_add_book)
def show_frame_view_books(frame_view_books):
    viewBooks(frame_view_books)
def show_frame_update_book(frame_update_book):
    updateBook(frame_update_book)
def show_frame_view_users(frame_view_users):
    viewUsers(frame_view_users)
def show_frame_add_user(frame_add_user):
    addUser(frame_add_user)
def show_frame_delete_user(frame_delete_user):
    deleteUser(frame_delete_user)
def show_frame_update_user(frame_update_user):
    updateUser(frame_update_user)
    # root
root = Tk()
root.title("Library Information Management System - Group 16")
root.geometry("1000x618")
root.resizable(False, False)
root.wm_attributes('-alpha', 0.85)
root.configure(background="black")

    # frames
frame_main = Frame(root, bg="black")
frame_main.place(relx=0, rely=0, relwidth=1, relheight=1)

frame_view_books = Frame(root, bg="black")
frame_view_books.place(relx=0, rely=0, relwidth=1, relheight=1)
frame_view_books.config(background="black")

frame_add_book = Frame(root, bg="black")
frame_add_book.place(relx=0, rely=0, relwidth=1, relheight=1)

frame_remove_book = Frame(root, bg="black")
frame_remove_book.place(relx=0, rely=0, relwidth=1, relheight=1)

frame_update_book = Frame(root, bg="black")
frame_update_book.place(relx=0, rely=0, relwidth=1, relheight=1)

frame_view_users = Frame(root, bg="black")
frame_view_users.place(relx=0, rely=0, relwidth=1, relheight=1)
frame_view_users.config(background="black")

frame_add_user = Frame(root, bg="black")
frame_add_user.place(relx=0, rely=0, relwidth=1, relheight=1)

frame_delete_user = Frame(root, bg="black")
frame_delete_user.place(relx=0, rely=0, relwidth=1, relheight=1)

frame_update_user = Frame(root, bg="black")
frame_update_user.place(relx=0, rely=0, relwidth=1, relheight=1)


    # buttons
view_books_icon = PhotoImage(file = r"Imgs/view_all_icon_2.png")
button1 = Button(frame_main, image=view_books_icon, bg='white', fg='black', bd=0,
                 command=lambda:show_frame_view_books(frame_view_books))
button1.place(relx=0.05, rely=0.1, relwidth=0.1, relheight=0.1)
view_books_label = Label(frame_main, text="View All Books", bg="black", fg="white")
view_books_label.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

add_book_icon = PhotoImage(file=r"Imgs/add_book_icon.png")
button3 = Button(frame_main, image=add_book_icon, text="Add Book", bg='black', fg='black', bd=0,
                 command=lambda:show_frame_add_book(frame_add_book))
button3.place(relx=0.20, rely=0.1, relwidth=0.1, relheight=0.1)
add_book_label = Label(frame_main, text="Add Book", bg="black", fg="white")
add_book_label.place(relx=0.2, rely=0.05, relwidth=0.1, relheight=0.05)

remove_book_icon = PhotoImage(file=r"Imgs/remove_book_icon.png")
button4 = Button(frame_main, image=remove_book_icon,text="Delete Book", bg='black', fg='black', bd=0,
                 command=lambda:deleteBook(frame_remove_book))
button4.place(relx=0.35, rely=0.1, relwidth=0.1, relheight=0.1)
remove_book_label = Label(frame_main, text="Remove Book", bg="black", fg="white")
remove_book_label.place(relx=0.35, rely=0.05, relwidth=0.1, relheight=0.05)

update_book_label = Label(frame_main, text="Update Book", bg="black", fg="white")
update_book_label.place(relx=0.2, rely=0.35, relwidth=0.1, relheight=0.05)
update_book_icon = PhotoImage(file=r"Imgs/update_book_icon.png")
button5 = Button(frame_main, image=update_book_icon, text="Update Book", bg='white', fg='black', bd=0,
                 command=lambda:show_frame_update_book(frame_update_book))
button5.place(relx=0.05, rely=0.25, relwidth=0.4, relheight=0.1)

view_users_icon = PhotoImage(file=r"Imgs/view_users_icon.png")
button6 = Button(frame_main, image=view_users_icon, text="View All Users", bg='white', fg='black',
                 command=lambda:show_frame_view_users(frame_view_users))
button6.place(relx=0.55, rely=0.1, relwidth=0.1, relheight=0.1)
view_books_label = Label(frame_main, text="View All Users", bg="black", fg="white")
view_books_label.place(relx=0.55, rely=0.05, relwidth=0.1, relheight=0.05)

add_user_icon = PhotoImage(file=r"Imgs/add_user_icon.png")
button7 = Button(frame_main, image=add_user_icon, text="Add User", bg='black', fg='black', bd=0,
                 command=lambda:show_frame_add_user(frame_add_user))
button7.place(relx=0.70, rely=0.1, relwidth=0.1, relheight=0.1)
add_user_label = Label(frame_main, text="Add User", bg="black", fg="white")
add_user_label.place(relx=0.70, rely=0.05, relwidth=0.1, relheight=0.05)

remove_user_icon = PhotoImage(file=r"Imgs/remove_user_icon.png")
button8 = Button(frame_main, image=remove_user_icon, text="Remove User", bg='black', fg='black', bd=0,
                 command=lambda:show_frame_delete_user(frame_delete_user))
button8.place(relx=0.85, rely=0.1, relwidth=0.1, relheight=0.1)
add_user_label = Label(frame_main, text="Delete User", bg="black", fg="white")
add_user_label.place(relx=0.85, rely=0.05, relwidth=0.1, relheight=0.05)

update_user_icon = PhotoImage(file=r"Imgs/update_user_icon.png")
button9 = Button(frame_main, image=update_user_icon, text="Update User", bg='white', fg='black',
                 command=lambda:show_frame_update_user(frame_update_user))
button9.place(relx=0.55, rely=0.25, relwidth=0.4, relheight=0.1)
update_user_label = Label(frame_main, text="Update User", bg="black", fg="white")
update_user_label.place(relx=0.70, rely=0.35, relwidth=0.1, relheight=0.05)

view_lent_label = Label(frame_main, text="View Lent", bg="black", fg="white")
view_lent_label.place(relx=0.05, rely=0.55, relwidth=0.1, relheight=0.05)
view_lent_icon = PhotoImage(file=r"Imgs/view_lent.png")
button10 = Button(frame_main, image=view_lent_icon, bg='white', fg='black', bd=0, command=viewLent)
button10.place(relx=0.05, rely=0.45, relwidth=0.1, relheight=0.1)

lend_label = Label(frame_main, text="Lend Book", bg="black", fg="white")
lend_label.place(relx=0.20, rely=0.55, relwidth=0.1, relheight=0.05)
lend_icon = PhotoImage(file=r"Imgs/lend_book_icon.png")
button11 = Button(frame_main, image=lend_icon, bg='white', fg='black', command=lendBook)
button11.place(relx=0.20, rely=0.45, relwidth=0.1, relheight=0.1)

return_book_label = Label(frame_main, text="Return Book", bg="black", fg="white")
return_book_label.place(relx=0.35, rely=0.55, relwidth=0.1, relheight=0.05)
return_book_icon = PhotoImage(file=r"Imgs/return_book_icon.png")
button12 = Button(frame_main, image=return_book_icon, bg='white', fg='black', command=returnBook)
button12.place(relx=0.35, rely=0.45, relwidth=0.1, relheight=0.1)

view_all_borrowers_icon = PhotoImage(file=r"Imgs/view_all_borrowers_icon.png")
button13 = Button(frame_main, image=view_all_borrowers_icon, bg='white', fg='black', command=viewBorrowers)
button13.place(relx=0.55, rely=0.45, relwidth=0.1, relheight=0.1)
view_borrowers_label = Label(frame_main, text="View Borrowers", bg="black", fg="white")
view_borrowers_label.place(relx=0.55, rely=0.55, relwidth=0.1, relheight=0.05)

view_borrower_by_name_icon = PhotoImage(file=r"Imgs/view_borrower_by_name_icon.png")
button14 = Button(frame_main, image=view_borrower_by_name_icon, bg='white', fg='black', command=viewBorrowerByName)
button14.place(relx=0.70, rely=0.45, relwidth=0.1, relheight=0.1)
view_borrower_by_name_label = Label(frame_main, text="Borrowers List", bg="black", fg="white")
view_borrower_by_name_label.place(relx=0.70, rely=0.55, relwidth=0.1, relheight=0.05)
view_borrower_by_name_label.config(font=("Calibri", 12))

view_borrower_by_book_icon = PhotoImage(file=r"Imgs/view_borrower_by_book_icon.png")
button15 = Button(frame_main, image=view_borrower_by_book_icon, bg='white', fg='black', command=viewBorrowersByBookName)
button15.place(relx=0.85, rely=0.45, relwidth=0.1, relheight=0.1)
view_borrower_by_book_label = Label(frame_main, text="Borrowers By Book", bg="black", fg="white")
view_borrower_by_book_label.place(relx=0.85, rely=0.55, relwidth=0.1, relheight=0.05)

    # unicode notepad
def save_note(note):
    # global saved
    try:
        saved = note.get(1.0, END)
        with io.open("notes.txt", 'w', encoding='utf8') as f:
            f.write(saved)
        messagebox.showinfo("Success!", saved)
    except:
        messagebox.showinfo("Error", "Can't save")
def get_note(note):
    # global saved
    try:
        with io.open("notes.txt", 'r', encoding='utf8') as f:
            saved = f.read()
            note.insert(index=END, chars=saved)
    except:
        messagebox.showinfo("Error", "Can't get notes")

note_label = Label(frame_main, text="Unicode Notepad", bg="black", fg="white")
note_label.place(relx=0.45, rely=0.58, relwidth=0.1, relheight=0.1)
note = Text(frame_main)
note.place(relx=0.1,rely=0.65, relwidth=0.85, relheight=0.3)

save_icon = PhotoImage(file=r"Imgs/save_icon.png")
button16 = Button(frame_main, image=save_icon, bg='white', fg='black',
                  command=lambda:save_note(note))
button16.place(relx=0.05, rely=0.65, relwidth=0.04, relheight=0.15)

down_icon = PhotoImage(file=r"Imgs/down_icon.png")
button17 = Button(frame_main, image=down_icon, bg='white', fg='black',
                  command=lambda:get_note(note))
button17.place(relx=0.05, rely=0.80, relwidth=0.04, relheight=0.15)

    # menu
# def our_command():
#     pass
# my_menu = Menu(frame_main)
# frame_main.config(menu=my_menu)
# file_menu = Menu(my_menu)
# my_menu.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New", command=our_command)
# my_menu.add_separator()
# my_menu.add_command(label="Exit", command=frame_main.quit)

# initialize GUI
show_frame_main(frame_main)
root.mainloop()