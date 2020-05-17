# SIMMail1.py

import RPi.GPIO as GPIO
import smtplib, datetime, os, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

USERNAME = 'raspi4kids@gmail.com'  # Username for authentication
PASSWORD = 'raspi1234'  # Password for authentication
SMTP_SERVER = 'smtp.gmail.com'  # URL of SMTP server

FROM = "Aegidius Pluess"  # Name shown as sender
TO = 'a2015@pluess.name' # Mail address of the recipient
SSL_PORT = 465

P_BUTTON = 24 # Button pin, adapt to your wiring

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(P_BUTTON, GPIO.IN, GPIO.PUD_UP)

def sendMail(subject, text, img = None):
    print("Sending the mail...")
    msg = MIMEMultipart("alternative")
    msg.attach(MIMEText(text, "html"))

    tmpmsg = msg
    msg = MIMEMultipart()
    msg.attach(tmpmsg)
    if img != None:
        if not os.path.exists(img):
            print "File", img, "does not exist." 
        else:
            fp = open(img, 'rb')
            img = MIMEImage(fp.read())  # included in mail, not as attachment
            fp.close()
            msg.attach(img)
    
    msg['Subject'] = subject
    msg['From'] = FROM
    server = smtplib.SMTP_SSL(SMTP_SERVER, SSL_PORT)
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROM, [TO], msg.as_string())
    server.quit()
    print("Mail successfully sent.")

setup()
print "Waiting for button event..."
while True:
    if GPIO.input(P_BUTTON) == GPIO.LOW:
        t = str(datetime.datetime.now())
        text = "Alert on " + t + "<br>Button was <b>pressed!</b>"        
        subject = "Alert from Raspberry Pi"
        sendMail(subject, text)
        #sendMail(subject, text, "c:/scratch/mailtest.png")
        time.sleep(30)


