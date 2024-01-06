

import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("yjonjale@gmail.com", "twta ogdc arbe gumt")
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("yjonjale@gmail.com", "yjonjale@gmail.com", message)
# terminating the session
s.quit()

print("email sent")

