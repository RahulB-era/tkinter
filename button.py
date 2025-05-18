import tkinter as tk
window = tk.Tk()
window.title("button")

num = 0

def click():
    global num
    print(num)
    num += 1

icon = tk.PhotoImage(file="bird.png")
button = tk.Button(window, text= "Click Me",
                   font=("roboto","20","bold"),
                     bg="black",   
                     fg="white",
                     activeforeground="black",
                     activebackground="white",
                     state=tk.NORMAL, # NORMAL, DISABLED
                    #  image=icon,
                     compound='top', # position of the image it make the text visible position relative to the text
                   command = click)
button.pack()



window.mainloop()