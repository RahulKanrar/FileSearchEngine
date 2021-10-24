import smtplib


# login notification sent to mail
def login_notification(receiver):
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login('1707214@kiit.ac.in', 'hyyj douo hcyj wlrd')
            subject = 'Welcome to Search Engine'
            body = 'Hey user!\n\nYou have been succesfully logged into the search engine powered by skill assure\n\nStart surfing in our search engine and Have a good time \n\nThankyou.'
            msg = f'Subject: {subject}\n\n{body}'
            smtp.sendmail('1707214@kiit.ac.in', receiver, msg)
    except:
        print("Email was not sent")
