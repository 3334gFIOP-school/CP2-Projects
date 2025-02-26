import smtplib

# Gmail's SMTP server and port

smtp_server = "smtp.gmail.com"
smtp_port = 587  # or 465 for SSL
user_email = "jackson.hauley@ucas-edu.net"
user_password = "dont look here"  


# Setting up the connection and login
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Secure the connection using TLS
server.login(user_email, user_password)

# Send an email (example)

sender = "jackson.hauley@ucas-edu.net"
recipient = "gavin.pierce@ucas-edu.net"
subject = "Hello"
body = "Your mom dot com"


y = 1
for x in range(10):
    subject = y
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender, recipient, message)
    y += 1

# Close the connection
server.quit()