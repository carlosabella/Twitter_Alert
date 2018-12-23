import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("carlosg.abella@gmail.com")
subject = "Novedades Twit Alert"
to_email = Email("carlosg.abella@gmail.com")
#content = Content("text/plain", "Contenido del email")

def sendEmail(cont):
    content = Content("text/plain", cont)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)