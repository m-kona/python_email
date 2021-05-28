import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'konamasibulele@gmail.com '
receiver_email_id = ('retshepilekoloko27@gmail.com','me.tsotetsi@gmail.com')
subject = 'Sending Email'
password = input("Enter senders email password")
# start TLS for security
s.starttls()