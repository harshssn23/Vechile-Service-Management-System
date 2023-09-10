from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1080x720")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background_12.png")
background = canvas.create_image(
    540.0, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"mechsubmit.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 475, y = 433,
    width = 131,
    height = 50)

img1 = PhotoImage(file = f"mechback.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 909, y = 622,
    width = 131,
    height = 50)

entry0_img = PhotoImage(file = f"workentry.png")
entry0_bg = canvas.create_image(
    540.0, 169.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 387, y = 140,
    width = 306,
    height = 57)

entry1_img = PhotoImage(file = f"workentry.png")
entry1_bg = canvas.create_image(
    540.0, 315.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 387, y = 286,
    width = 306,
    height = 57)

window.resizable(False, False)
window.mainloop()
