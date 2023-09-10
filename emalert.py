import smtplib
from email.message import EmailMessage

def email_alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = 'vsmsp6@gmail.com'
    msg['from'] = user
    password = 'zxtpnmgnknyxohjs'

    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,password)
    server.send_message(msg)

    server.quit()

#email_alert('test',"test msg don't reply","sanjithvikraman1@gmail.com")