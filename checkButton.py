import tkinter as tk
window = tk.Tk()
window.title("CheckBox")

def display():
    if(x.get() ==1):
        print("Checked")
    else:
        print("Unchecked")
img = tk.PhotoImage(file="check.png")
x = tk.IntVar()
checkbox = tk.Checkbutton(window, text="Check me out",
                          variable = x,
                          onvalue = 1,
                          offvalue = 0,
                          command= display,
                          font="Arial 20",
                          fg = "#00ff00",
                          bg = "black",
                          padx= 20,
                          pady= 20,
                          image= img,
                          actigevebackground = "black",
                          activeforeground = "#00ff00",)

checkbox.pack()

window.mainloop()