# three different layouts

# 1. Grid layout
# 2. Place layout
# 3. Pack layout

import tkinter as tk
window = tk.Tk()
window.title("Layout Example")  
window.geometry("300x200")

label1 =  tk.Label(window, text= "Label 1")
entry1 = tk.Entry(window)
label2 =  tk.Label(window, text= "Label 2")
entry2 = tk.Entry(window)
button1 = tk.Button(window, text = "Button 1")
button2 = tk.Button(window, text = "Button 2")

#pack layout
# label1.pack( padx=5, pady=5, side=tk.LEFT)
# entry1.pack( padx=5, pady=5, side=tk.LEFT)
# label2.pack( padx=5, pady=5)
# entry2.pack()
# button1.pack()
# button2.pack()

#grid
label1.grid(row=0, column=0, padx=5, pady=5)
entry1.grid(row=0, column=1, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5, columnspan =2)
entry2.grid(row=1, column=1, padx=5, pady=5, rowspan=2)

window.mainloop()