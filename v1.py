from tkinter import *
from custclass import Customer
import json
from tkcalendar import Calendar
from tkinter import messagebox
from serviceclass import service
from tkinter import ttk
from admin import *
from datetime import *
from datetime import date,datetime
from emalert import email_alert
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from fpdf import FPDF


ad=Admin()
window=Tk()
window.geometry("1080x720")

def getname(ps):
    with open("data.json","r") as cfile:
        ccdata=json.load(cfile)
        for i in ccdata:
            if i['phone']==ps.cust:
                return i['name']
def getmail(ps):
    with open("data.json","r") as cfile:
        ccdata=json.load(cfile)
        for i in ccdata:
            if i['phone']==ps.cust:
                return i['mail']

def report(work,window,ps,ps1):
    def v():
        pdfc(getname(ps),ps.model,ps.regnon,ee1.get(),ee2.get(),ee3.get(),ps1["type"],ee4.get(),ee5.get(),"jobcard"+str(ps.cust)+".pdf",ps)
        messagebox.showinfo("Success","Jobcard is generated successfully")

    def submit():
        e1 = ee1.get()
        e2 = ee2.get()
        e4 = ee4.get()  
        if (e1.isdigit()) == False or (e2.isdigit()) == False or (e4.isdigit()) == False or int(e1) <= 0 or e2.startswith("-") or e2.startswith("0") or int(e4) <= 0:
            messagebox.showwarning(title='WARNING!',message='Enter appropriate values for the given fields! ')
        else:
            v() 
    window.destroy()
    window=Tk()
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
        command = submit,
        relief = "flat")

    b1.place(
        x = 460, y = 514,
        width = 116,
        height = 43)

    window.resizable(False, False)
    window.mainloop()
    # l1=Label(window,text="Odumeter reading")
    # l1.place(x=100,y=20)
    # ee1=Entry(window)
    # ee1.place(x=300,y=20)
    # l2=Label(window,text="Fuel level")
    # l2.place(x=100,y=70)
    # ee2=Entry(window)
    # ee2.place(x=300,y=70)
    # l3=Label(window,text="Test drive")
    # l3.place(x=100,y=120)
    # ee3=Entry(window)
    # ee3.place(x=300,y=120)
    # l4=Label(window,text='price')
    # l4.place(x=100,y=170)
    # ee4=Entry(window)
    # ee4.place(x=300,y=170)
    # l5=Label(window,text='Line about service')
    # l5.place(x=100,y=220)
    # ee5=Entry(window)
    # ee5.place(x=300,y=220)
    # gen=Button(window,text="GENERATE",command=v)
    # gen.place(x=300,y=270)
    # backbtn=Button(window,text="BACK",command=lambda:work(window))
    # backbtn.place(x=300,y=320)


def servfinished1(window):
    with open("ww1.json","r") as wfile:
        wdet=json.load(wfile)
        if not wdet:
            messagebox.showinfo(title='INFORMATION!',message='No Job is pending!')  

        ps1=wdet.pop(0)
        
    with open("ww1.json","w") as wfile:
        json.dump(wdet,wfile)
    ps=w1._works.dequeue()
    report(work1,window,ps,ps1)


def work1(window):
    window.destroy()
    window=Tk()
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
        command = lambda:servfinished1(window),
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
        command = lambda:workerlogin(window),
        relief = "flat")

    b1.place(
        x = 909, y = 622,
        width = 131,
        height = 50)
    
    
    treetab1("ww1.json",w1,window,0,0)

    window.resizable(False, False)
    window.mainloop()

def servfinished2(window):
    with open("ww2.json","r") as wfile:
        wdet=json.load(wfile)
        if not wdet:
            messagebox.showinfo(title='INFORMATION!',message='No Job is pending!')
        ps1=wdet.pop(0)
    with open("ww2.json","w") as wfile:
        json.dump(wdet,wfile)
    ps=w2._works.dequeue()
    report(work2,window,ps,ps1)

def work2(window):
    window.destroy()
    window=Tk()
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
        command = lambda:servfinished2(window),
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
        command = lambda:workerlogin(window),
        relief = "flat")

    b1.place(
        x = 909, y = 622,
        width = 131,
        height = 50)
    
    
    treetab1("ww2.json",w2,window,0,0)

    window.resizable(False, False)
    window.mainloop()

def servfinished3(window):
    with open("ww3.json","r") as wfile:
        wdet=json.load(wfile)
        if not wdet:
            messagebox.showinfo(title='INFORMATION!',message='No Job is pending!')
        ps1=wdet.pop(0)
    with open("ww3.json","w") as wfile:
        json.dump(wdet,wfile)
    ps=w3._works.dequeue()
    report(work3,window,ps,ps1)

def work3(window):
    window.destroy()
    window=Tk()
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
        command = lambda:servfinished3(window),
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
        command = lambda:workerlogin(window),
        relief = "flat")

    b1.place(
        x = 909, y = 622,
        width = 131,
        height = 50)
    
    
    treetab1("ww3.json",w3,window,0,0)

    window.resizable(False, False)
    window.mainloop()
    

def servfinished4(window):
    with open("ww4.json","r") as wfile:
        wdet=json.load(wfile)
        if not wdet:
            messagebox.showinfo(title='INFORMATION!',message='No Job is pending!')
        ps1=wdet.pop(0)
    with open("ww4.json","w") as wfile:
        json.dump(wdet,wfile)
    ps=w4._works.dequeue()
    report(work4,window,ps,ps1)

def work4(window=None):
    if window is not None:
        window.destroy()
    window=Tk()
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
        command = lambda:servfinished4(window),
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
        command = lambda:workerlogin(window),
        relief = "flat")

    b1.place(
        x = 909, y = 622,
        width = 131,
        height = 50)
    
    
    treetab1("ww4.json",w4,window,0,0)

    window.resizable(False, False)
    window.mainloop()

def servfinished5(window):
    with open("ww5.json","r") as wfile:
        wdet=json.load(wfile)
        if not wdet:
            messagebox.showinfo(title='INFORMATION!',message='No Job is pending!')
        ps1=wdet.pop(0)
    with open("ww5.json","w") as wfile:
        json.dump(wdet,wfile)
    ps=w5._works.dequeue()
    report(work5,window,ps,ps1)

def work5(window):
    if window is not None:
        window.destroy()
    window=Tk()
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
        command = lambda:servfinished5(window),
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
        command = lambda:workerlogin(window),
        relief = "flat")

    b1.place(
        x = 909, y = 622,
        width = 131,
        height = 50)
    
    
    treetab1("ww5.json",w5,window,0,0)

    window.resizable(False, False)
    window.mainloop()

def workerlogin(p):

    def submitw():
        if llbl11.get()=="w1" and llbl21.get()=="w1":
            work1(window)
        elif llbl11.get()=="w2" and llbl21.get()=="w2":
            work2(window)
        elif llbl11.get()=="w3" and llbl21.get()=="w3":
            work3(window)
        elif llbl11.get()=="w4" and llbl21.get()=="w4":
            work4(window)
        elif llbl11.get()=="w5" and llbl21.get()=="w5":
            work5(window)
        else:
            reply1 = messagebox.askretrycancel("Invalid login","Invalid username or password")
            if reply1 == False:
                reply2 = messagebox.askyesno("Confirmation" , message = "Are you sure you want to cancel? ")
                if reply2 == True:
                    homepage(window)

    def submit():
        if len(llbl11.get()) == 0:
            messagebox.showwarning(title='WARNING!',message='User name has not been entered!') 
        if len(llbl11.get()) == 0:
            messagebox.showwarning(title='WARNING!',message='Password has not been entered!')
        if len(llbl11.get()) != 0 and len(llbl21.get()) != 0:
            submitw()

    
    if p is not None:
        p.destroy()
    
    window = Tk()
    window.title("Worker Login")
    window.geometry('1080x720')
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
        command = submit,
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
        command = lambda:homepage(window),
        relief = "flat")

    b1.place(
        x = 909, y = 622,
        width = 131,
        height = 50)

    entry0_img = PhotoImage(file = f"workentry.png")
    entry0_bg = canvas.create_image(
        540.0, 169.5,
        image = entry0_img)

    llbl11 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"))

    llbl11.place(
        x = 387, y = 140,
        width = 306,
        height = 57)

    entry1_img = PhotoImage(file = f"workentry.png")
    entry1_bg = canvas.create_image(
        540.0, 315.5,
        image = entry1_img)

    llbl21 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,font=("Regular", 16, "bold"),
        show="*")

    llbl21.place(
        x = 387, y = 286,
        width = 306,
        height = 57)

    window.resizable(False, False)
    window.mainloop()
def pdfmail(filejobcard,r_email= "custmailssn@gmail.com"):
    sender_email = "vsmsp6@gmail.com"
    receiver_email = r_email
    message = MIMEMultipart()
    message["From"] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Service Job card"
    file = filejobcard
    attachment = open(file,'rb')
    obj = MIMEBase('application','octet-stream')
    obj.set_payload((attachment).read())
    encoders.encode_base64(obj)
    obj.add_header('Content-Disposition',"attachment; filename= "+file)
    message.attach(obj)
    my_message = message.as_string()
    email_session = smtplib.SMTP('smtp.gmail.com',587)
    email_session.starttls()
    email_session.login(sender_email,'zxtpnmgnknyxohjs')
    email_session.sendmail(sender_email,receiver_email,my_message)
    email_session.quit()
    print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")

def pdfc(a,c,d,e,f,g,h,i,j,k,ps):

    pdf=FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size = 12)

    pdf.cell(200,10,txt = "Vehicle Job Card",ln=1,align = 'C')
    pdf.cell(200,10,txt = "Date: "+str(date.today()),ln=2,align = 'R')
    pdf.cell(200,10,txt = "Customer Name:      "+str(a),ln=3,align = 'L')
    #pdf.cell(200,10,txt = "Vehicle Brand:"+str(b),ln=4,align = 'L')
    pdf.cell(200,10,txt = "Vehicle Model:      "+str(c),ln=5,align = 'L')
    pdf.cell(200,10,txt = "Registration Number:"+str(d),ln=6,align = 'L')
    pdf.cell(200,10,txt = "Odometer reading:   "+str(e),ln=7,align = 'L')
    pdf.cell(200,10,txt = "Fuel level:         "+str(f),ln=8,align = 'L')
    pdf.cell(200,10,txt = "Test Drive:         "+str(g),ln=9,align = 'L')
    pdf.cell(200,10,txt = "Service work done:  "+str(h),ln=10,align = 'L')
    pdf.cell(200,10,txt = "Price:              "+str(i),ln=10,align = 'L')
    pdf.cell(200,10,txt = "About the service   "+str(j),ln=11,align = 'L')


    pdf.output(k)
    #pdfmail(k)
    pdfmail(k,getmail(ps))


def treetab1(filename,workername,window,a,b):
    www=Label(window,text=workername).place(x=30,y=20+b)
    with open(filename,'r') as file:
        service_data=json.load(file)
        for serv in service_data:
            #print(serv["bdate"])
            workername._works.enqueue(service(serv['cust'],serv['model'],serv["regno"],serv['type'][0],serv["bdate"],serv["rdate"],serv["worker"]))
        treev = ttk.Treeview(window, selectmode ='browse')
 
        treev.place(x=125,y=25+b)
        verscrlbar = ttk.Scrollbar(window,orient ="vertical",command = treev.yview)

        verscrlbar.place(x=1030,y=50+b)

        treev.configure(xscrollcommand = verscrlbar.set)
 
        treev["columns"] = ("1", "2", "3","4","5","6","7")
 
        treev['show'] = 'headings'
        treev['height']=3

        treev.column("1", width = 100, anchor ='c')
        treev.column("2", width = 100, anchor ='se')
        treev.column("3", width = 100, anchor ='se')
        treev.column("4", width = 100, anchor ='se')
        treev.column("5", width = 100, anchor ='se')
        treev.column("6", width = 100, anchor ='se')
        treev.column("7", width = 100, anchor ='se')        
 

        treev.heading("1", text ="Customer Id")
        treev.heading("2", text ="Model")
        treev.heading("3", text ="Regno")
        treev.heading("4", text ="Servicetype")
        treev.heading("5", text ="Date1")
        treev.heading("6", text ="Rdate")
        treev.heading("7", text ="Worker")

        for dic in workername._works:
            treev.insert("",'end',text="l",values=(dic.cust,dic.model,dic.regnon,dic.stype,dic.bodate,dic.rddate,workername._id))

def adwork1(window):
    window.destroy()
    window=Tk()
    window.title("w1")
    window.geometry('1080x720')
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

    background_img = PhotoImage(file = f"background_11.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    img0 = PhotoImage(file = f"custde back.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:worker_details(window),
        relief = "flat")

    b0.place(
        x = 909, y = 622,
        width = 131,
        height = 50)

    lbl2=Label(window,text="Pending Services").place(x=50,y=50)
    treetab("ww1.json",w1,window,100,100)

    window.resizable(False, False)
    window.mainloop()

def adwork2(window):
    window.destroy()
    window=Tk()
    window.title("w2")
    window.geometry('1080x720')
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

    background_img = PhotoImage(file = f"background_11.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    img0 = PhotoImage(file = f"custde back.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:worker_details(window),
        relief = "flat")

    b0.place(
        x = 909, y = 622,
        width = 131,
        height = 50)
    lbl2=Label(window,text="Pending Services").place(x=50,y=50)
    treetab("ww2.json",w2,window,100,100)

    window.resizable(False, False)
    window.mainloop()

def adwork3(window):
    window.destroy()
    window=Tk()
    window.title("w3")
    window.geometry('1080x720')
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

    background_img = PhotoImage(file = f"background_11.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    img0 = PhotoImage(file = f"custde back.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:worker_details(window),
        relief = "flat")

    b0.place(
        x = 909, y = 622,
        width = 131,
        height = 50)
    lbl2=Label(window,text="Pending Services").place(x=50,y=50)
    treetab("ww3.json",w3,window,100,100)

    window.resizable(False, False)
    window.mainloop()

def adwork4(window):
    window.destroy()
    window=Tk()
    window.title("w4")
    window.geometry('1080x720')
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

    background_img = PhotoImage(file = f"background_11.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    img0 = PhotoImage(file = f"custde back.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:worker_details(window),
        relief = "flat")

    b0.place(
        x = 909, y = 622,
        width = 131,
        height = 50)
    lbl2=Label(window,text="Pending Services").place(x=50,y=50)
    treetab("ww4.json",w4,window,100,100)

    window.resizable(False, False)
    window.mainloop()

def adwork5(window):
    window.destroy()
    window=Tk()
    window.title("w5")
    window.geometry('1080x720')
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

    background_img = PhotoImage(file = f"background_11.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    img0 = PhotoImage(file = f"custde back.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:worker_details(window),
        relief = "flat")

    b0.place(
        x = 909, y = 622,
        width = 131,
        height = 50)

    lbl2=Label(window,text="Pending Services").place(x=50,y=50)
    treetab("ww5.json",w5,window,100,100)

    window.resizable(False, False)
    window.mainloop()

def worker_details(window):
    def workerdisplay(w_id):
        if w_id=="w1":
            adwork1(window)
        elif w_id=="w2":
            adwork2(window)
        elif w_id=="w3":
            adwork3(window)
        elif w_id=="w4":
            adwork4(window)
        elif w_id=="w5":
            adwork5(window)
        else:
            messagebox.askretrycancel("Invalid id","Try Again")
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
        command =lambda:workerdisplay(entry0.get()),
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

def custde(window):
    window.destroy()
    window=Tk()
    window.title("Customer")
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

    background_img = PhotoImage(file = f"background_11.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    img0 = PhotoImage(file = f"custde back.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:adlogin_next(window),
        relief = "flat")

    b0.place(
        x = 909, y = 622,
        width = 131,
        height = 50)
    
    search_btn=Label(window,text="REGISTERED CUSTOMERS").place(x=21,y=21)
    with open('data.json','r') as file:
        cust_data=json.load(file)
        for customers in cust_data:
            ad.custlist.insert(Customer(customers["name"],customers["mail"],customers["phone"],customers['pwd']))
        treev = ttk.Treeview(window, selectmode ='browse')
 
        treev.place(x=50,y=50)
        verscrlbar = ttk.Scrollbar(window,orient ="vertical",command = treev.yview)

        verscrlbar.place(x=600,y=200)

        treev.configure(xscrollcommand = verscrlbar.set)
 
        treev["columns"] = ("1", "2", "3")
 
        treev['show'] = 'headings'

        treev.column("1", width = 150, anchor ='c')
        treev.column("2", width = 150, anchor ='se')
        treev.column("3", width = 150, anchor ='se')
 

        treev.heading("1", text ="Name")
        treev.heading("2", text ="Email")
        treev.heading("3", text ="Phone")
        for dic in ad.custlist:
            treev.insert("",'end',text="l",values=(dic.name,dic.mail,dic.phone))

    window.resizable(False, False)
    window.mainloop()

def spage(p):
    if p is not None:
        p.destroy()

    window=Tk()
    window.title("Services page")
    window.geometry('1080x720')
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

    background_img = PhotoImage(file = f"background_11.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    with open('service.json','r') as file:
        service_data=json.load(file)
        for serv in service_data:
            print(serv["bdate"])
            ad.totalservices.insert(service(serv['cust'],serv['model'],serv["regno"],serv['type'][0],serv["bdate"],serv["rdate"],serv["worker"]))
        treev = ttk.Treeview(window, selectmode ='browse')
 
        treev.place(x=0,y=100)
        verscrlbar = ttk.Scrollbar(window,orient ="vertical",command = treev.yview)

        verscrlbar.place(x=1060,y=200)

        treev.configure(xscrollcommand = verscrlbar.set)
 
        treev["columns"] = ("1", "2", "3","4","5","6","7")
 
        treev['show'] = 'headings'

        treev.column("1", width = 150, anchor ='c')
        treev.column("2", width = 150, anchor ='se')
        treev.column("3", width = 150, anchor ='se')
        treev.column("4", width = 150, anchor ='se')
        treev.column("5", width = 150, anchor ='se')
        treev.column("6", width = 150, anchor ='se')
        treev.column("7", width = 150, anchor ='se')        
 

        treev.heading("1", text ="Customer Id")
        treev.heading("2", text ="Model")
        treev.heading("3", text ="Regno")
        treev.heading("4", text ="Servicetype")
        treev.heading("5", text ="Date1")
        treev.heading("6", text ="Rdate")
        treev.heading("7", text ="Worker")

        for dic in ad.totalservices:
            treev.insert("",'end',text="l",values=(dic.cust,dic.model,dic.regnon,dic.stype,dic.bodate,dic.rddate,dic.worker))
    
    img0 = PhotoImage(file = f"custde back.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:adlogin_next(window),
        relief = "flat")

    b0.place(
        x = 909, y = 622,
        width = 131,
        height = 50)

    window.resizable(False, False)
    window.mainloop()

def pspage(window):
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

    background_img = PhotoImage(file = f"background_11.png")
    background = canvas.create_image(
        540.0, 360.0,
        image=background_img)

    treetab("ww1.json",w1,window,0,0)
    treetab("ww2.json",w2,window,0,100)
    treetab("ww3.json",w3,window,0,200)
    treetab("ww4.json",w4,window,0,300)
    treetab("ww5.json",w5,window,0,400)

    img0 = PhotoImage(file = f"custde back.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:adlogin_next(window),
        relief = "flat")

    b0.place(
        x = 909, y = 622,
        width = 131,
        height = 50)
    
    window.resizable(False, False)
    window.mainloop()

    # back=Button(window,text="Back",command=lambda:adlogin_next(window)).place(x=1450,y=500)


def treetab(filename,workername,window,a,b):
    www=Label(window,text=workername).place(x=30,y=20+b)
    with open(filename,'r') as file:
        service_data=json.load(file)
        for serv in service_data:
            #print(serv["bdate"])
            workername._works.enqueue(service(serv['cust'],serv['model'],serv["regno"],serv['type'][0],serv["bdate"],serv["rdate"],serv["worker"]))
        treev = ttk.Treeview(window, selectmode ='browse')
 
        treev.place(x=125,y=25+b)
        verscrlbar = ttk.Scrollbar(window,orient ="vertical",command = treev.yview)

        verscrlbar.place(x=900,y=50+b)

        treev.configure(xscrollcommand = verscrlbar.set)
 
        treev["columns"] = ("1", "2", "3","4","5","6","7")
 
        treev['show'] = 'headings'
        treev['height']=3

        treev.column("1", width = 100, anchor ='c')
        treev.column("2", width = 100, anchor ='se')
        treev.column("3", width = 100, anchor ='se')
        treev.column("4", width = 100, anchor ='se')
        treev.column("5", width = 100, anchor ='se')
        treev.column("6", width = 100, anchor ='se')
        treev.column("7", width = 100, anchor ='se')        
 

        treev.heading("1", text ="Customer Id")
        treev.heading("2", text ="Model")
        treev.heading("3", text ="Regno")
        treev.heading("4", text ="Servicetype")
        treev.heading("5", text ="Date1")
        treev.heading("6", text ="Rdate")
        treev.heading("7", text ="Worker")

        for dic in workername._works:
            treev.insert("",'end',text="l",values=(dic.cust,dic.model,dic.regnon,dic.stype,dic.bodate,dic.rddate,workername._id))


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
        command = lambda:spage(window),
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
        command = lambda:custde(window),
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
        command =lambda:pspage(window),
        relief = "flat")

    b4.place(
        x = 436, y = 331,
        width = 205,
        height = 50)

    window.resizable(False, False)
    window.mainloop()

def adlogin_page(window):
    
    def check(window):
        if entry0.get()=="admin" and entry1.get()=="1234":
            adlogin_next(window)
        else:
            reply1 = messagebox.askretrycancel("Invalid login","Invalid username or password")
            if reply1 == False:
                reply2 = messagebox.askyesno("Confirmation" , message = "Are you sure you want to cancel? ")
                if reply2 == True:
                    homepage(window)


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

    def submit():
        
        if len(entry0.get()) == 0: 
            messagebox.showwarning(title='WARNING!',message='Username has not been entered!')
        if len(entry1.get()) == 0: 
            messagebox.showwarning(title='WARNING!',message='Password has not been entered!') 
        if len(entry0.get()) != 0 and len(entry1.get()) != 0 :
            check(window) 

    img0 = PhotoImage(file = f"submit2.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = submit,
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
        highlightthickness = 0,font=("Regular", 16, "bold"))

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
        highlightthickness = 0,font=("Regular", 16, "bold"),
        show  = '*')

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

    def submit():
        
        e_m = newemail.get() 
        
        if len(e_m) == 0:
            messagebox.showwarning(title='WARNING!',message='Email has not been entered!') 
        if len(e_m) != 0 and e_m.find('@') == -1:
            messagebox.showwarning(title='WARNING!',message='Enter a valid Email ID!')
        if len(newname.get()) == 0: 
            messagebox.showwarning(title='WARNING!',message='Name has not been entered!')
        if len(newpwd.get()) == 0: 
            messagebox.showwarning(title='WARNING!',message='Password has not been entered!') 
        if len(e_m) != 0 and len(newname.get()) != 0 and len(newpwd.get()) != 0 and e_m.find('@') != -1:
            changedata(window,newname.get(),newemail.get(),custphone,newpwd.get())  


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
        highlightthickness = 0,font=("Regular", 16, "bold"),
        show = '*')

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
        command = submit,
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

    def submit():
        if len(brand.get()) == 0: 
            messagebox.showwarning(title='WARNING!',message='Vehicle brand has not been entered!')
        if len(model.get()) == 0: 
            messagebox.showwarning(title='WARNING!',message='Model has not been entered!')
        if len(regno.get()) == 0: 
            messagebox.showwarning(title='WARNING!',message='Registration number has not been entered!') 
        if len(brand.get()) != 0 and len(model.get()) != 0 and len(regno.get()) != 0:
            servicebook(window,phone,brand.get(),model.get(),regno.get(),type,cal.selection_get())


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
        command = submit,
        relief = "flat")

    b0.place(
        x = 475, y = 622,
        width = 131,
        height = 50)

    window.resizable(False, False)
    window.mainloop()

def servicebook(window,phone,brand,model,regno,type,bkdate):

    with open('servicedate.json','r') as servicedatefile:
            datesi=json.load(servicedatefile)
    with open('data.json','r') as file:
        details=json.load(file)
    for i in details:
        if str(i.get('phone'))==phone:
            recmail=str(i.get('mail'))
            recname=str(i.get('name'))
    if datesi.count(str(bkdate))>0:
        messagebox.showwarning(title='warning',message='Slot unavailable,book another date!!')
    else:
        with open('servicedate.json','w') as servicedatefile:
            datesi.append(str(bkdate))
            json.dump(datesi,servicedatefile)
        with open("service.json","r") as serfile:
            sercount=json.load(serfile)
        if len(sercount)%5==0:
            cust_service=service(phone,str(model)+" "+str(brand),regno,type,bkdate,bkdate+timedelta(2),"w1")
            cust_service.writefile("ww1.json",phone)
        elif len(sercount)%5==1:
            cust_service=service(phone,str(model)+" "+str(brand),regno,type,bkdate,bkdate+timedelta(2),"w2")
            cust_service.writefile("ww2.json",phone)
        elif len(sercount)%5==2:
            cust_service=service(phone,str(model)+" "+str(brand),regno,type,bkdate,bkdate+timedelta(2),"w3")
            cust_service.writefile("ww3.json",phone)
        elif len(sercount)%5==3:
            cust_service=service(phone,str(model)+" "+str(brand),regno,type,bkdate,bkdate+timedelta(2),"w4")
            cust_service.writefile("ww4.json",phone)
        elif len(sercount)%5==4:
            cust_service=service(phone,str(model)+" "+str(brand),regno,type,bkdate,bkdate+timedelta(2),"w5")
            cust_service.writefile("ww5.json",phone)
        cust_service.addServicetype(type)
        cust_service.writefile('service.json',phone)

        messagebox.showinfo(title='Successful',message='Slot Booked!!')

        #Email integrated

        text='Hi '+str(recname)+'\n'
        text+='Thanks for choosing our service!\nAs per Your service booking on '
        text+=str(datetime.today())+','
        text+='\nYour vechicle details:'
        text+='\n'+str(model+brand)
        text+='\n'+str(regno)
        text+='\n'+'Service type: '+str(type)
        text+='\nKindly hand over you vehicle on'
        text+=' '+str(bkdate)+'\nEstimated return date: '+str(bkdate+timedelta(2))
        email_alert('Service Booked',text,recmail)

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

    def submit():

        m = mobile.get()
        if len(m) == 0: 
            messagebox.showwarning(title='WARNING!',message='Mobile number has not been entered!') 
        if (m.isdigit() == False) and len(m) != 0: 
            messagebox.showwarning(title='WARNING!',message='Enter a valid mobile number!')
        if len(m) != 0 and len(m) != 10:
            messagebox.showwarning(title='WARNING!',message='Mobile number must contain 10 digits!')
        if len(password.get()) == 0: 
            messagebox.showwarning(title='WARNING!',message='Password has not been entered!') 
        if len(m) == 10 and (m.isdigit()) and len(password.get()) != 0:
            login_check(window,mobile.get(),password.get())
       
    

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
        highlightthickness = 0,font=("Regular", 16, "bold"),
        show = '*')

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
        command = submit,
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
                    break
        else:
            messagebox.showerror(title = 'ERROR!',
            message=' Incorrect phone number/password! ')

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

    def submit():
        e_m = email.get() 
        ph = phone.get()
        with open('data.json','r') as file:
             cust_data=json.load(file)
             for customers in cust_data:
                 #print("before if")
                 #print (customers["name"] ,  n)
                 #print(customers["phone"],ph)
                 #if (customers["name"])==n and customers["phone"] == ph:
                 if (customers["phone"]) == ph:   
                    messagebox.showinfo(title='ALREADY A CUSTOMER',message='  Redirecting to login page...  ')
                    loginpage(window)
                       
                       
        if len(name.get()) == 0: 
            messagebox.showwarning(title='WARNING!',message='First name has not been entered!')
        if len(e_m) == 0:
            messagebox.showwarning(title='WARNING!',message='Email has not been entered!') 
        if len(e_m) != 0 and e_m.find('@') == -1:
            messagebox.showwarning(title='WARNING!',message='Enter a valid Email ID!')
        if len(ph) == 0: 
            messagebox.showwarning(title='WARNING!',message='Mobile number has not been entered!')
        if (ph.isdigit() == False) and len(ph) != 0: 
            messagebox.showwarning(title='WARNING!',message='Enter a valid mobile number!')
        if len(ph) != 0 and len(ph) != 10:
            messagebox.showwarning(title='WARNING!',message='Mobile number must contain 10 digits!')
        if len(pwd.get()) == 0: 
            messagebox.showwarning(title='WARNING!',message='Password has not been entered!') 
        if len(name.get()) != 0 and len(e_m) != 0 and e_m.find('@') != -1 and len(ph) == 10 and (ph.isdigit()) and len(pwd.get()) != 0:
            dataupdate(window)           



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
        highlightthickness = 0,font=("Regular", 16, "bold"),show='*')

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
        command = submit ,
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
        command =lambda:workerlogin(window),
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
