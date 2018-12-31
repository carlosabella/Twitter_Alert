import sendgrid
import os
from sendgrid.helpers.mail import *

emailaddress = os.environ.get('EMAIL_DEFAULT')
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email(emailaddress)

def sendEmail(cont, dt, membername, toemailaddress):
    to_email = Email(toemailaddress)
    subject = membername + " Twit Alert " + "(" + dt + ")"
    content = Content("text/plain", cont)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)