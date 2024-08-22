from django.core.mail import send_mail

send_mail(
    "Subject here",
    "Here is the message.",
    "burhon439@gmail.com",
    ["burhon439@gmail.com"],
    fail_silently=False,
)