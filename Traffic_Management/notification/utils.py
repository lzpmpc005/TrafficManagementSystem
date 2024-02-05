from django.conf import settings
from django.core.mail import send_mail

def send_email_with_smtp(subject, message, recipient):
    try: 
        if type(recipient) == str:
            recipient = [recipient]

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipient,
        )
    except Exception as e:
        print(e)
