from django.core.mail import send_mail

def send_confirmation_email(email, code, title, price):
    full_link = f'Hello, confirm your order for product {title} for {price} \nTap this -> http://localhost:8000/api/v1/order/confirm/{code}'    
    send_mail(
        f'Order confirm',
        full_link,
        'dcabatar@gmail.com',
        [email]
    )