import tkinter as tk
window = tk.Tk()
window.title("entry")

num = 0

def click():
    global num
    print(num)
    num += 1

def submit():
    print(entry.get()) # get the text from the entry
    entry.delete(0,tk.END) # start address and end address of the entry
    entry.delete(len(entry.get())-1,tk.END) # start address and end address of the entry
    # entry.config(state=tk.DISABLED)

entry = tk.Entry(window,
                 font=("roboto","20","bold"),
                 show="+"
                )
entry.pack(side=tk.LEFT, padx=10, pady=10) # side = tk.LEFT, tk.RIGHT, tk.TOP, tk.BOTTOM

button = tk.Button(window, text="Submit", command=submit )
button.pack(side=tk.LEFT)

entry.insert(0,"Enter the fucking name")

window.mainloop() 