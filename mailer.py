import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown
import ssl

def read_body_from_file(filename, format="plain"):
    """Reads email body from a file and converts Markdown if specified."""
    with open(filename, "r") as file:
        body = file.read()
    if format == "markdown":
        body = markdown.markdown(body)
    return body

# Email credentials and settings
sender_email = "yash.jonjale@iitb.ac.in"  # Replace with your email
passwprd=""
smtp_server = "smtp-auth.iitb.ac.in"
smtp_server1="smtp.gmail.com" 
port = 587
subject = "Looking for internship opportunities : Auf der Suche nach Praktikumsmöglichkeiten"
input_format = input("Enter email body format (plain/markdown): ")


# Load recipient email addresses from a file
recipients=['yjonjale@gmail.com', 'yashjonjale@cse.iitb.ac.in', 'borgwardt@biochem.mpg.de','']

print(recipients)
# Read email body based on chosen format
if input_format.lower() == "markdown":
    body = read_body_from_file("email_body.md", format="markdown")
else:
    body = read_body_from_file("email_body.txt")
print(body)
# Create email message
# Create email message (using HTML for Markdown content)
message = MIMEMultipart()
message["From"] = sender_email
message["Subject"] = subject
message.attach(MIMEText(body, "html" if input_format.lower() == "markdown" else "plain"))

# Send emails
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)

    
    server.sendmail(sender_email, recipients, message.as_string())

print("Emails sent successfully!")
