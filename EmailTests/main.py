import smtplib

# Gmail's SMTP server and port
smtp_server = "smtp.gmail.com"
smtp_port = 587  # or 465 for SSL

user_email = "jackson.hauley@ucas-edu.net"
user_password = "set later"  

# Setting up the connection and login
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Secure the connection using TLS
server.login(user_email, user_password)

# Send an email (example)
sender = "your_email@gmail.com"
recipient = "recipient_email@example.com"
subject = "Test"
body = "This is a test email."

message = f"Subject: {subject}\n\n{body}"

server.sendmail(sender, recipient, message)

# Close the connection
server.quit()