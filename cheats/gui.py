from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def calculate(*args):  # Work to do when button press
    try:
        value = float(feet.get())  # get data
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)  # calculate
    except ValueError:
        #messagebox.showerror("Windows title", "error message")
        messagebox.showerror("Error", "You must introduce a valid number")
        feet.set("")


root = Tk()  # create windows
root.title("Feet to Meters")  # set title

mainframe = ttk.Frame(root, padding="3 3 12 12")  # window padding
mainframe.grid(column=3, row=3, sticky=(N, W, E, S))  # layout

# internal variables of I/O widgets
feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(
    mainframe, width=7, textvariable=feet)  # input text widget
feet_entry.grid(column=2, row=1, sticky=(W, E))  # add to view

# Create and add the button. Asociate it with the function calculate
ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W)

# Create and add the labels
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# add padding to each element
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()  # initial focus
root.bind('<Return>', calculate)  # enter will calculate

root.mainloop()  # display windows (this blocks the threat
