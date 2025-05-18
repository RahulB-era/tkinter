import tkinter as tk
window = tk.Tk()
window.title("my app")
window.geometry("400x400")

icon = tk.PhotoImage(file="bird.png")
window.iconphoto(True, icon) #true to set the icon for the window and taskbar not only window

window.config(background="black") # set the background color of the window
label = tk.Label(window, 
                text="Hello World", 
                    font="arial 20",
                    bg="black",
                    fg="white",
                    relief=tk.RAISED,
                    bd=5,
                    image = icon,
                    compound='bottom', # position of the image
                    padx=20, # padding x
                )
label.place(x=0,y=0)
# label.pack()

window.mainloop()