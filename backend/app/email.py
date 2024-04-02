from models import models
from database.dependency import db_dependency
import smtplib

def getemail(db: db_dependency):
    
    Email = db.query(models.Email).all()
    return Email

def addemail(email, db: db_dependency):
    Email = models.Email(user_id=email.user_id, 
                       matrix_id=email.matrix_id, 
                       client_name = email.client_name, 
                       status_of_email=email.status_of_email,
                       )
    db.add(Email)
    db.commit()
    send_email(email)
    return {"message": "Email Added."}

def send_email(SendEmail):

    print(SendEmail)
    host = 'karmamgmt.icewarpcloud.in'
    from_email = SendEmail.sender
    to_email = SendEmail.receiver
    # karmamgmt.icewarpcloud.in
    # outgoing port 25
    # incoming port 143

    # host = 'smtp.office365.com'
    # from_email = SendEmail.sender
    # to_email = SendEmail.receiver
    message_subject = "disturbance in sector 7"
    message_text = "Three are dead in an attack in the sewers below sector 7."
    message = "From: %s\r\n" % from_email + "To: %s\r\n" % to_email + "Subject: %s\r\n" % message_subject + "\r\n" + message_text
    print(message)
    server = smtplib.SMTP(host, 25)
    server.ehlo()
    server.starttls()
    server.set_debuglevel(1)
    server.sendmail(from_email, to_email, message) 
    server.quit()



    return {"message": "Email sent."}
