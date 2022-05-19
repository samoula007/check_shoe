import smtplib

# send the mail


def send(sender, password, target, subject, message):

    server = smtplib.SMTP('smtp.mailgun.org', 587)
    server.ehlo()
    server.starttls()

    server.login(sender, password)

    server.sendmail(
        sender, target, subject + "\n\n" + message)
    server.close()
