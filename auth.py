import uuid
import smtplib, ssl

#--------------------------------------------------------------------------------------------

def rn(string_length=10):
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return random[0:string_length]


#--------------------------------------------------------------------------------------------

port = 587
smtp_server = "smtp.gmail.com"
sender_email = "your gmail"
receiver_email = "receiver gmail"
password = "your gmail password"
message = (rn(7))

#--------------------------------------------------------------------------------------------

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

#--------------------------------------------------------------------------------------------

code = input("Input code that has been sent to your gmail account: ")

#--------------------------------------------------------------------------------------------

if message == code:
    print("The code which you entered is right")
else:
    print("The code which you entered is wrong")