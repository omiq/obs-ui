# modules
import tkinter as tk
from PIL import Image, ImageTk


def button_click():
    """
    respond to the button click
    """
    print("well it was clicked, what now?")


root = tk.Tk()

# create a frame and pack it
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, fill=tk.X)

# load icons
image1 = Image.open("button.png")
photo1 = ImageTk.PhotoImage(image1)

# create the image button, image is above (top) the optional text
button1 = tk.Button(frame1, compound=tk.TOP, width=155, height=55, image=photo1,
    text="optional text", bg='green', command=button_click)
button1.pack(side=tk.LEFT, padx=2, pady=2)
# save the button's image from garbage collection (needed?)
button1.image = photo1
# start the event loop
root.mainloop()