from django.core.mail import send_mail


def send_confirmation_email(email, code):
    # import time
    # time.sleep(5)
    full_link = f'http://localhost:8000/api/v1/account/activate/{code}'
    send_mail(
        'Активация пользователя',
        full_link,
        'dcabatar@gmail.com',
        [email]
    )


def send_confirmation_code(email, code):
    send_mail(
        'Восстановление пароля',
        code,
        'dcabatar@gmail.com',
        [email]
    )