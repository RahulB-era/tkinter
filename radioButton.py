import tkinter as tk
window = tk.Tk()
window.title("RadioButton")
def order():
    if (x.get() == 1):
        print("Pizza")
    elif (x.get() == 2):
        print("Burger")
    elif (x.get() == 3):
        print("Ice Cream") 
    elif (x.get() == 4):
        print("Pasta")

food = [ "Pizza", "Burger", "Ice Cream", "Pasta"]
pizzaImage = tk.PhotoImage(file='pizza.png')
hamburgesrImage = tk.PhotoImage(file='hamburger.png')
hamburgerImage = tk.PhotoImage(file='hambsurger.png')
hotdogImage = tk.PhotoImage(file='hotdog.png')
foodImages = [pizzaImage, hamburgerImage, hotdogImage, hamburgesrImage]
x = tk.IntVar()

for index in range(len(food)):
    radioButton = tk.Radiobutton(window, text = food[index], #add text to radion button
                                 variable = x, #groups them
                                    value = index, #value of the radio button
    image = foodimages[index], #image of the radio button
    compound = tk.LEFT, #position of the image
    indicatoron=0, #remove the circle
    bg = "black", #background color
    width= 200, #width of the radio button
    command= order
    )
    radioButton.pack( anchor=tk.W) #anchor to the west

window.mainloop()