from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import search




def calculate(*args):   #Work to do when button press
    try:
        keywordV = keyword.get()
        numberV =  number.get()
        search.do_search(keywordV, numberV)
        messagebox.showerror("Ok", "Data processed")
    except ValueError:
        # messagebox.showerror("Windows title", "error message")
        messagebox.showerror("Error", "Incorrect data format")


root = Tk()  # create windows
root.title("Image downloader")  # set title

# internal variables of I/O widgets
keyword = StringVar()
number = IntVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")  # window padding
mainframe.grid(column=2, row=3, sticky=(N, W, E, S))  # layout

ttk.Label(mainframe, text="Keyword").grid(column=1, row=1, sticky=W)

keyword_entry = ttk.Entry(mainframe, width=7, textvariable=keyword)  # input text widget
keyword_entry.grid(column=2, row=1, sticky=(W, E))  # add to view

ttk.Label(mainframe, text="Number of images").grid(column=1, row=2, sticky=W)

number_entry = Spinbox(mainframe, from_=1, to=101, textvariable=number)  # input text widget
number_entry.grid(column=2, row=2, sticky=(W, E))  # add to view

# Create and add the button. Asociate it with the function calculate
ttk.Button(mainframe, text="Do it", command=calculate).grid(column=2, row=3, sticky=E)

# add padding to each element
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

keyword_entry.focus()  # initial focus
root.bind('<Return>', calculate)  # enter will calculate



def open_ui():
    root.mainloop()  # display windows (this blocks the threat

if __name__ == "__main__":
    open_ui()