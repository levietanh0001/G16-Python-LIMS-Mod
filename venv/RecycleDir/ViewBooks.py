from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import pymysql
from ScrollableFrameClass import *
    
def view():

        # database details
    my_pass = "123321"
    my_db = "g16_db"

        # connect to database
    con = pymysql.connect(host="localhost", user="root", password=my_pass, database=my_db, port=3306)
    cur = con.cursor()
    book_table = "books"

        # main window
    root = Tk()
    root.title("View All Books")
    root.geometry("500x500")

        # create canva
    cv = Canvas(root)
    cv.config(bg="black")
    cv.pack(expand=True,fill=BOTH)

    headingLabel = Label(root, text="View Books", bg='black', fg='white', font=('Courier',15))
    headingLabel = Label(root, text="View Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    data_frame = Frame(root, bg='black')
    data_frame.place(relx=0,rely=0,relwidth=0.9,relheight=0.9)
    y = 0.25

        # díplay book table header
    Label(data_frame, text="%-10s %-30s %-30s %-30s" % ('Book ID','Title','Author','Status'), bg='black',fg='white')\
        .place(relx=0.01, rely=0.05)
    Label(data_frame, text="----------------------------------------------------------------------------",bg='black',fg='white')\
        .place(relx=0.01,rely=0.15)
    get_books = "select * from " + book_table

        # error message if unable to get books
    try:
        cur.execute(get_books)
        con.commit()
            # retrieve every book detail
        for i in cur:
            Label(data_frame, text="%-10s %-30s %-30s %-30s" % (i[0],i[1],i[2],i[3]),bg='black',fg='white')\
                .place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch files from database")

    quit_button = Button(root, text="Quit", bg='white', fg='black', command=root.destroy)
    quit_button = Button(root, text="Quit", bg='white', fg='black', command=root.destroy)
    quit_button.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)


    root.mainloop()