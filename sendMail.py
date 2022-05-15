import smtplib


def send(sender, password, target, subject, message):

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender, password)

    server.sendmail(
        sender, target, subject + "\n\n" + message)
