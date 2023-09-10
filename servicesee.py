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

background_img = PhotoImage(file = f"background_13.png")
background = canvas.create_image(
    540.0, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"finishservice.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 444, y = 609,
    width = 191,
    height = 63)

img1 = PhotoImage(file = f"backservice.png")
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

window.resizable(False, False)
window.mainloop()
