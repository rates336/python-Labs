import smtplib
import functools


def send_info_email(user, password, mail_from, mail_to, mail_subject, mail_body):
    # mail_from = 'Your automation system'
    # mail_to = ['newslattery@gmail.com', 'karolstepniewski23@gmail.com']
    # mail_subject = 'test'
    # mail_body = 'Here enter some text'
    message = '''From: {}
Subject: {}    

{}
'''.format(mail_from, mail_subject, mail_body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        try:
            server.sendmail(user, mail_to, message)
            print('All it\'s ok, mail was send to {}'.format(mail_to))
        except:
            print('Try send mail has been failure')
        server.close()
    except:
        print('Something went wrong while attempt connect to server')


user_1 = 'newslattery@gmail.com'
password_1 = 'ahroyduxnxgiojfs'
mail_from_1 = 'Learning Python system'
short_smInfo = functools.partial(send_info_email, user_1, password_1, mail_from_1, mail_subject='Learning sm in Python')
short_smInfo('ilearninghere.karol@gmail.com', mail_body='It\' s a test')

