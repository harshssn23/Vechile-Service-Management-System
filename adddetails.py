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

background_img = PhotoImage(file = f"background_14.png")
background = canvas.create_image(
    540.0, 360.0,
    image=background_img)

entry0_img = PhotoImage(file = f"adddetentry.png")
entry0_bg = canvas.create_image(
    518.5, 117.0,
    image = entry0_img)

ee1 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

ee1.place(
    x = 382, y = 89,
    width = 273,
    height = 54)

entry1_img = PhotoImage(file = f"adddetentry.png")
entry1_bg = canvas.create_image(
    518.5, 372.0,
    image = entry1_img)

ee4 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

ee4.place(
    x = 382, y = 344,
    width = 273,
    height = 54)

entry2_img = PhotoImage(file = f"adddetentry.png")
entry2_bg = canvas.create_image(
    518.5, 457.0,
    image = entry2_img)

ee5 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

ee5.place(
    x = 382, y = 429,
    width = 273,
    height = 54)

entry3_img = PhotoImage(file = f"adddetentry.png")
entry3_bg = canvas.create_image(
    518.5, 287.0,
    image = entry3_img)

ee3 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

ee3.place(
    x = 382, y = 259,
    width = 273,
    height = 54)

entry4_img = PhotoImage(file = f"adddetentry.png")
entry4_bg = canvas.create_image(
    518.5, 202.0,
    image = entry4_img)

ee2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

ee2.place(
    x = 382, y = 174,
    width = 273,
    height = 54)

img0 = PhotoImage(file = f"detback.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:work(window),
    relief = "flat")

b0.place(
    x = 923, y = 634,
    width = 116,
    height = 43)

img1 = PhotoImage(file = f"detsubmit.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = v,
    relief = "flat")

b1.place(
    x = 460, y = 514,
    width = 116,
    height = 43)

window.resizable(False, False)
window.mainloop()
