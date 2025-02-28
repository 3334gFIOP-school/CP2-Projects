import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

smtp_server = "smtp.gmail.com"
smtp_port = 587  # or 465 for SSL
user_email = "jackson.hauley@ucas-edu.net"
user_password = "e"  
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls() 
server.login(user_email, user_password)
sender = "jackson.hauley@ucas-edu.net"
recipient = "gavin.pierce@ucas-edu.net"
subject = "E"
body = "Hello"
file_path = "C:/Users/jackson.hauley/Downloads/random sound.mp3"

y = 1
for x in range(5):
    subject = str(y)  # Ensure subject is a string
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    # Attach body text
    message.attach(MIMEText(body, "plain"))

    # Attach file
    try:
        with open(file_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={file_path.split('/')[-1]}")  
        message.attach(part)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

    # Send the email
    server.sendmail(sender, recipient, message.as_string())
    y += 1
    print(f"Email {y-1} sent")

# Close the connection
server.quit()