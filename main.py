# Importing libraries
from tkinter import *
from tkinter import messagebox

# Creating and setting up the window
window = Tk()
window.geometry("500x400")
window.title("Virus Scan")

# Creating the command and function
def msg_box():
    messagebox.showwarning("Alert", "Stop! Virus found")

def show_info():
    messagebox.showinfo("Information", "This is about tkinter")

# Creating buttons
btn1 = Button(master=window, text="Scan for virus", command=msg_box, bg="orange", fg="white", relief="groove")
btn1.place(x=210, y=210)
btn2 = Button(master=window, text="Click for Info", command=show_info, bg="green", fg="light blue", relief="ridge")
btn2.place(x=210, y=180)

# Calling the main loop of tkinter
window.mainloop()