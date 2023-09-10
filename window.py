from tkinter import *
from tkcalendar import Calendar


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

background_img = PhotoImage(file = f"background_10.png")
background = canvas.create_image(
    555.0, 360.0,
    image=background_img)

img0 = PhotoImage(file = f"bkslot.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 475, y = 622,
    width = 131,
    height = 50)

img1 = PhotoImage(file = f"bck.png")
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

entry0_img = PhotoImage(file = f"bkslotentry.png")
entry0_bg = canvas.create_image(
    539.5, 233.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 419, y = 210,
    width = 241,
    height = 44)

entry1_img = PhotoImage(file = f"bkslotentry.png")
entry1_bg = canvas.create_image(
    539.5, 160.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 419, y = 137,
    width = 241,
    height = 44)

entry2_img = PhotoImage(file = f"bkslotentry.png")
entry2_bg = canvas.create_image(
    539.5, 87.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 419, y = 64,
    width = 241,
    height = 44)

cal = Calendar()
cal.place(x = 419, y = 300)

window.resizable(False, False)
window.mainloop()
