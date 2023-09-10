from tkinter import *
from custclass import Customer
import json
from tkcalendar import Calendar
from tkinter import messagebox
from serviceclass import service

window=Tk()
window.geometry("1080x720")

def worker_details(window):
    window.destroy()

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

    background_img = PhotoImage(file = f"background_9.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"entrybox.png")
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

    img0 = PhotoImage(file = f"search.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        #command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 474, y = 247,
        width = 131,
        height = 50)

    img1 = PhotoImage(file = f"back4.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:adlogin_next(window),
        relief = "flat")

    b1.place(
        x = 950, y = 646,
        width = 116,
        height = 50)

    window.resizable(False, False)
    window.mainloop()

def adlogin_next(window):
    window.destroy()

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

    background_img = PhotoImage(file = f"background_8.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    img0 = PhotoImage(file = f"back4.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:adlogin_page(window),
        relief = "flat")

    b0.place(
        x = 950, y = 646,
        width = 116,
        height = 50)

    img1 = PhotoImage(file = f"sd.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        #command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 436, y = 226,
        width = 205,
        height = 50)

    img2 = PhotoImage(file = f"cd.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        #command = btn_clicked,
        relief = "flat")

    b2.place(
        x = 436, y = 121,
        width = 205,
        height = 50)

    img3 = PhotoImage(file = f"wd.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:worker_details(window),
        relief = "flat")

    b3.place(
        x = 437, y = 436,
        width = 205,
        height = 50)

    img4 = PhotoImage(file = f"ps.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        #command = btn_clicked,
        relief = "flat")

    b4.place(
        x = 436, y = 331,
        width = 205,
        height = 50)

    window.resizable(False, False)
    window.mainloop()

def adlogin_page(window):
    window.destroy()

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

    background_img = PhotoImage(file = f"background_7.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    img0 = PhotoImage(file = f"submit2.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:adlogin_next(window),
        relief = "flat")

    b0.place(
        x = 475, y = 433,
        width = 131,
        height = 50)

    img1 = PhotoImage(file = f"back3.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:homepage(window),
        relief = "flat")

    b1.place(
        x = 909, y = 622,
        width = 131,
        height = 50)

    entry0_img = PhotoImage(file = f"ad_entry.png")
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

    entry1_img = PhotoImage(file = f"ad_entry.png")
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

def editprofile_page(window,custphone):
    window.destroy()

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

    background_img = PhotoImage(file = f"background_6.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"entrybox.png")
    entry0_bg = canvas.create_image(
        540.0, 281.5,
        image = entry0_img)

    newemail = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    newemail.place(
        x = 387, y = 252,
        width = 306,
        height = 57)

    entry1_img = PhotoImage(file = f"entrybox.png")
    entry1_bg = canvas.create_image(
        540.0, 169.5,
        image = entry1_img)

    newname = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    newname.place(
        x = 387, y = 140,
        width = 306,
        height = 57)

    entry2_img = PhotoImage(file = f"entrybox.png")
    entry2_bg = canvas.create_image(
        540.0, 393.5,
        image = entry2_img)

    newpwd = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    newpwd.place(
        x = 387, y = 364,
        width = 306,
        height = 57)

    img0 = PhotoImage(file = f"back2.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:after_login(window,custphone),
        relief = "flat")

    b0.place(
        x = 945, y = 635,
        width = 105,
        height = 48)

    img1 = PhotoImage(file = f"submit1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:changedata(window,newname.get(),newemail.get(),custphone,newpwd.get()),
        relief = "flat")

    b1.place(
        x = 475, y = 454,
        width = 129,
        height = 48)

    window.resizable(False, False)
    window.mainloop()

def changedata(window,name,email,mobile,pwd):

    newcust=Customer(name,email,mobile,pwd)
    dict1=newcust.createdict()

    newcust.updatefile('data.json',mobile,dict1)

    after_login(window,mobile)


def bkservice_page(window,custphone):
    window.destroy()

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

    background_img = PhotoImage(file = f"background_5.png")
    background = canvas.create_image(
        540.0, 357.0,
        image=background_img)

    img0 = PhotoImage(file = f"back1.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:after_login(window,custphone),
        relief = "flat")

    b0.place(
        x = 950, y = 646,
        width = 116,
        height = 50)

    img2 = PhotoImage(file = f"RR.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:bookslot_page(window,custphone,'Running Repairs'),
        relief = "flat")

    b2.place(
        x = 436, y = 121,
        width = 205,
        height = 50)

    img3 = PhotoImage(file = f"ins.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:bookslot_page(window,custphone,'Inspection'),
        relief = "flat")

    b3.place(
        x = 106, y = 408,
        width = 205,
        height = 50)

    img4 = PhotoImage(file = f"tyr.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:bookslot_page(window,custphone,'Tyre services'),
        relief = "flat")

    b4.place(
        x = 766, y = 408,
        width = 205,
        height = 50)

    img5 = PhotoImage(file = f"batt.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:bookslot_page(window,custphone,'Battery check'),
        relief = "flat")

    b5.place(
        x = 436, y = 408,
        width = 205,
        height = 50)

    img6 = PhotoImage(file = f"break.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:bookslot_page(window,custphone,'Breaks'),
        relief = "flat")

    b6.place(
        x = 766, y = 121,
        width = 205,
        height = 50)

    img7 = PhotoImage(file = f"PM.png")
    b7 = Button(
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:bookslot_page(window,custphone,'Periodic Maintenance'),
        relief = "flat")

    b7.place(
        x = 106, y = 121,
        width = 205,
        height = 50)

    window.resizable(False, False)
    window.mainloop()

def bookslot_page(window,phone,type):
    window.destroy()

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

    img1 = PhotoImage(file = f"bck.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:bkservice_page(window,phone),
        relief = "flat")

    b1.place(
        x = 909, y = 622,
        width = 131,
        height = 50)

    entry0_img = PhotoImage(file = f"bkslotentry.png")
    entry0_bg = canvas.create_image(
        539.5, 233.0,
        image = entry0_img)

    regno = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    regno.place(
        x = 419, y = 210,
        width = 241,
        height = 44)

    entry1_img = PhotoImage(file = f"bkslotentry.png")
    entry1_bg = canvas.create_image(
        539.5, 160.0,
        image = entry1_img)

    brand = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    brand.place(
        x = 419, y = 137,
        width = 241,
        height = 44)

    entry2_img = PhotoImage(file = f"bkslotentry.png")
    entry2_bg = canvas.create_image(
        539.5, 87.0,
        image = entry2_img)

    model = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    model.place(
        x = 419, y = 64,
        width = 241,
        height = 44)

    cal = Calendar()
    cal.place(x = 419, y = 300)

    img0 = PhotoImage(file = f"bkslot.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:servicebook(window,phone,brand.get(),model.get(),regno.get(),type,cal.selection_get()),
        relief = "flat")

    b0.place(
        x = 475, y = 622,
        width = 131,
        height = 50)

    window.resizable(False, False)
    window.mainloop()

def servicebook(window,phone,brand,model,regno,type,bkdate):

    with open('servicedate.json','r') as servicedatefile:
            dates=json.load(servicedatefile)
    if dates.count(str(bkdate))>0:
        messagebox.showwarning(title='warning',message='Slot unavailable,book another date!!')
    else:
        with open('servicedate.json','w') as servicedatefile:
            dates.append(str(bkdate))
            json.dump(dates,servicedatefile)

        cust_service=service(model+' '+brand,regno,bkdate)
        cust_service.addServicetype(type)
        cust_service.writefile('service.json',phone)

        messagebox.showinfo(title='Successful',message='Slot Booked!!')

        bkservice_page(window,phone)

def after_login(window,custphone):

    window.destroy()

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

    background_img = PhotoImage(file = f"background_4.png")
    background = canvas.create_image(
        495.0, 360.0,
        image=background_img)

    img0 = PhotoImage(file = f"bkservice.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:bkservice_page(window,custphone),
        relief = "flat")

    b0.place(
        x = 434, y = 329,
        width = 212,
        height = 52)

    img1 = PhotoImage(file = f"back_big.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:loginpage(window),
        relief = "flat")

    b1.place(
        x = 909, y = 622,
        width = 131,
        height = 50)

    img2 = PhotoImage(file = f"editprofile.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:editprofile_page(window,custphone),
        relief = "flat")

    b2.place(
        x = 434, y = 202,
        width = 212,
        height = 52)

    window.resizable(False, False)
    window.mainloop()


def loginpage(window):
    
    window.destroy()

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

    background_img = PhotoImage(file = f"background_3.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        540.0, 296.0,
        image = entry0_img)

    password = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    password.place(
        x = 369, y = 263,
        width = 342,
        height = 64)

    entry1_img = PhotoImage(file = f"img_textBox1.png")
    entry1_bg = canvas.create_image(
        540.0, 146.0,
        image = entry1_img)

    mobile = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    mobile.place(
        x = 369, y = 113,
        width = 342,
        height = 64)

    img0 = PhotoImage(file = f"back.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:cust_login(window),
        relief = "flat")

    b0.place(
        x = 947, y = 627,
        width = 102,
        height = 41)

    img1 = PhotoImage(file = f"login.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:login_check(window,mobile.get(),password.get()),
        relief = "flat")

    b1.place(
        x = 489, y = 405,
        width = 102,
        height = 41)

    window.resizable(False, False)
    window.mainloop()

def login_check(window,mobile,password):
    
    with open('data.json','r') as file:
        cust_data=json.load(file)
        for data in cust_data:
            if str(data.get('phone')) == mobile and data.get('pwd') == password:
                    after_login(window,mobile)

def cust_login(window):
    
    window.destroy()

    global name
    global email
    global phone
    global pwd

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

    background_img = PhotoImage(file = f"background_2.png")
    background = canvas.create_image(
        561.5, 338.5,
        image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox2.png")
    entry0_bg = canvas.create_image(
        518.5, 202.0,
        image = entry0_img)

    email = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    email.place(
        x = 382, y = 174,
        width = 273,
        height = 54)

    entry1_img = PhotoImage(file = f"img_textBox2.png")
    entry1_bg = canvas.create_image(
        518.5, 117.0,
        image = entry1_img)

    name = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    name.place(
        x = 382, y = 89,
        width = 273,
        height = 54)

    entry2_img = PhotoImage(file = f"img_textBox2.png")
    entry2_bg = canvas.create_image(
        518.5, 372.0,
        image = entry2_img)

    pwd = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    pwd.place(
        x = 382, y = 344,
        width = 273,
        height = 54)

    entry3_img = PhotoImage(file = f"img_textBox2.png")
    entry3_bg = canvas.create_image(
        518.5, 287.0,
        image = entry3_img)

    phone = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    phone.place(
        x = 382, y = 259,
        width = 273,
        height = 54)

    img0 = PhotoImage(file = f"back.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:homepage(window),
        relief = "flat")

    b0.place(
        x = 923, y = 634,
        width = 116,
        height = 43)

    img1 = PhotoImage(file = f"login.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:loginpage(window),
        relief = "flat")

    b1.place(
        x = 454, y = 634,
        width = 116,
        height = 43)

    img2 = PhotoImage(file = f"signup.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command =lambda:dataupdate(window) ,
        relief = "flat")

    b2.place(
        x = 454, y = 439,
        width = 116,
        height = 43)

    window.resizable(False, False)
    window.mainloop()


def homepage(window):
    window.destroy()
    
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

    background_img = PhotoImage(file = f"background_1.png")
    background = canvas.create_image(
        568.0, 358.0,
        image=background_img)

    img0 = PhotoImage(file = f"adlog.png")
    adlogbut = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:adlogin_page(window),
        relief = "flat")

    adlogbut.place(
        x = 611, y = 315,
        width = 261,
        height = 58)

    img1 = PhotoImage(file = f"mechlog.png")
    mechlogbut = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        #command = btn_clicked,
        relief = "flat")

    mechlogbut.place(
        x = 611, y = 419,
        width = 261,
        height = 58)

    img2 = PhotoImage(file = f"custlog.png")
    custlogbut = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:cust_login(window),
        relief = "flat")

    custlogbut.place(
        x = 611, y = 211,
        width = 261,
        height = 58)

    window.resizable(False, False)
    window.mainloop()

def dataupdate(window):

    cust=Customer(name.get(),email.get(),phone.get(),pwd.get())
    dict1=cust.createdict()
    cust.writefile('data.json',dict1)

    after_login(window,phone.get())

homepage(window)
window.mainloop()