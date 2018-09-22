# modules
import time
import tkinter as tk
from PIL import Image, ImageTk


# initialise tk
root = tk.Tk()


# function to send the key data
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


# click event
def button_click(caller):
    print("Button: {} was clicked, sending keypress".format(caller))

    if "button1" == caller:
        write_report("\0\0\4\0\0\0\0\0")
    elif "button2" == caller:
        write_report("\0\0\5\0\0\0\0\0")
    elif "button3" == caller:
        write_report("\0\0\6\0\0\0\0\0")
    elif "button4" == caller:
        write_report("\0\0\7\0\0\0\0\0")
    elif "button5" == caller:
        write_report("\0\0\10\0\0\0\0\0")
    else:
        write_report("\0\0\11\0\0\0\0\0")

    time.sleep(0.2)
    write_report("\0\0\0\0\0\0\0\0")


# load icons
image = Image.open("a.png")
photoa = ImageTk.PhotoImage(image)

image = Image.open("b.png")
photob = ImageTk.PhotoImage(image)

image = Image.open("c.png")
photoc = ImageTk.PhotoImage(image)

image = Image.open("d.png")
photod = ImageTk.PhotoImage(image)

image = Image.open("e.png")
photoe = ImageTk.PhotoImage(image)

image = Image.open("f.png")
photof = ImageTk.PhotoImage(image)



# add buttons
button1 = tk.Button(root, compound=tk.CENTER, image=photoa, text="Button 1", command=lambda: button_click('button1'))
button1.grid(row=0, column=0)

button2 = tk.Button(root, compound=tk.CENTER, image=photob, text="Button 2", command=lambda: button_click('button2'))
button2.grid(row=0, column=1)

button3 = tk.Button(root, compound=tk.CENTER, image=photoc, text="Button 3", command=lambda: button_click('button3'))
button3.grid(row=0, column=2)

button4 = tk.Button(root, compound=tk.CENTER, image=photod, text="Button 4", command=lambda: button_click('button4'))
button4.grid(row=1, column=0)

button5 = tk.Button(root, compound=tk.CENTER, image=photoe, text="Button 5", command=lambda: button_click('button5'))
button5.grid(row=1, column=1)

button6 = tk.Button(root, compound=tk.CENTER, image=photof, text="Button 6", command=lambda: button_click('button6'))
button6.grid(row=1, column=2)


# start the event loop
root.mainloop()