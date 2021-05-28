from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from Database.ConnectToMySQL import *

con = pymysql.connect(host=db_obj.get_host(), user=db_obj.get_user(),
                      password=db_obj.get_pass(), database=db_obj.get_db(),
                      port=db_obj.get_port())
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" #Issue Table
bookTable = "books" #Book Table


allBid = [] #List To store all Book IDs

def retB():
    

    book_id = bookID.get()
    copies = int(borrowNum.get())
    user_id = userID.get()

    try:
        args = [book_id, user_id, copies]
        cur.callproc('ReturnBook', args)
        con.commit()
        messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")

    root.destroy()
    
def returnBook(): 
    
    global root, con, cur, cv
    global bookID, userID, borrowNum
    
    root = Tk()
    root.title("Return Book")
    root.minsize(width=100, height=500)
    root.geometry("500x309")

    # name of book table
    book_table = "books"

    # create canva
    cv = Canvas(root)
    cv.config(bg="black")
    cv.pack(expand=True, fill=BOTH)

    # book id
    lb1 = Label(root, text="Book ID ", bg='black', fg='white')
    lb1.place(relx=0.01, rely=0.1, relheight=0.08)

    # book id query
    bookID = Entry(root)
    bookID.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # book title
    lb2 = Label(root, text="User ID ", bg='black', fg='white')
    lb2.place(relx=0.01, rely=0.25, relheight=0.08)

    # book title query
    userID = Entry(root)
    userID.place(relx=0.3, rely=0.25, relwidth=0.62, relheight=0.08)

    # author
    lb3 = Label(root, text="Copies Borrowed ", bg='black', fg='white')
    lb3.place(relx=0.01, rely=0.40, relheight=0.08)

    # author id query
    borrowNum = Entry(root)
    borrowNum.place(relx=0.3, rely=0.40, relwidth=0.62, relheight=0.08)

    # submit button
    submit_button = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=retB)
    submit_button.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    # quit button
    quit_button = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quit_button.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    # initialize GUI
    root.mainloop()