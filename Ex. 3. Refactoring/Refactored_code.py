import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class Mail:

    def __init__(self):
        self.login = 'login@gmail.com'
        self.password = 'qwerty'

    def send_message(self):
        subject = 'Subject'
        recipients = ['vasya@email.com', 'petya@email.com']
        message = 'Message'
        gmail_smtp = "smtp.gmail.com"

        email_message = MIMEMultipart()
        email_message['From'] = self.login
        email_message['To'] = ', '.join(recipients)
        email_message['Subject'] = subject
        email_message.attach(MIMEText(message))

        ms = smtplib.SMTP(gmail_smtp, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, ms, email_message.as_string())
        ms.quit()

    def receive_message(self):
        gmail_imap = "imap.gmail.com"
        header = None

        mail = imaplib.IMAP4_SSL(gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


if __name__ == '__main__':
    mailer = Mail()
