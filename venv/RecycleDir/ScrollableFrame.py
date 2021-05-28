import tkinter as tk
from tkinter import ttk
import pymysql
from tkinter import messagebox

    # database details
my_pass = "123321"
my_db = "g16_db"

    # connect to database
con = pymysql.connect(host="localhost",user="root",password=my_pass,database=my_db, port=3306)
cur = con.cursor()

book_table = "books"

    # root
root = tk.Tk()

    # container - Frame object
container = ttk.Frame(root)
    # canvas - Canvas object inside container (a Frame)
canvas = tk.Canvas(container)
    # scrollbar - a Scrollbar object inside container (a Frame)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    # a Frame object, 'inside' Canvas
scrollable_frame = ttk.Frame(canvas)

    # dynamically adjust frame size
scrollable_frame.bind(
        # whenever the frame changes size
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)
    # implement scrollable frame inside the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # scrollbar moves whenever canvas y-pos changes
canvas.configure(yscrollcommand=scrollbar.set)

# for i in range(50):
#     ttk.Label(scrollable_frame, text="Text fafasf dsafdsaf adfdf").pack()

get_books = "select * from " + book_table

    # error message if unable to get books
try:
    cur.execute(get_books)
    con.commit()
        # retrieve every book detail
    for i in cur:
        ttk.Label(scrollable_frame, text="%s %s %s %s" % (i[0], i[1], i[2], i[3])).pack()
        # y += 0.1
except:
    messagebox.showinfo("Failed to fetch files from database")

container.pack()
    # canvas + scrollbar = entire frame
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
