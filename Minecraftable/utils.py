from django.template import loader

from Minecraftable.printer import print_info


def get_matrix_from_request_post(request_post, matrix_name : str):
    recipe = []
    i = 0
    key = matrix_name + "[" + str(i) + "][]"
    while key in request_post:
        recipe.append(request_post.getlist(key))
        i += 1
        key = matrix_name + "[" + str(i) + "][]"
    
    return recipe


def next_alpha(s):
    return chr((ord(s.upper()) + 1 - 65) % 26 + 65)


def first_from_dict(dict):
    items_view = dict.items()
    value_iterator = iter(items_view)
    return next(value_iterator)  


from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

def reset_password_send(base_path, username, email):
    from django.core.mail import EmailMessage

    message = loader.get_template('Minecraftable/User/reset-template.html').render({
        'data': urlsafe_base64_encode(force_bytes({'username': username})),
        'name': 'password',
        'path': base_path,
    })
    from Minecraftable.admin import EMAIL_ADMIN
    mail = EmailMessage(
        subject='Password Reset',
        body=message,
        from_email=EMAIL_ADMIN,
        to=[email],
        reply_to=[],
    )
    mail.content_subtype = 'html'
    mail.send()


def reset_email_send(base_path, username, email):
    from django.core.mail import EmailMessage

    message = loader.get_template('Minecraftable/User/reset-template.html').render({
        'data': urlsafe_base64_encode(force_bytes({'username': username})),
        'name': 'email',
        'path': base_path,
    })
    from Minecraftable.admin import EMAIL_ADMIN
    mail = EmailMessage(
        subject='Email Reset',
        body=message,
        from_email=EMAIL_ADMIN,
        to=[email],
        reply_to=[],
    )
    mail.content_subtype = 'html'
    mail.send()


def send_confirmation_email(base_path, username, email):
    from django.core.mail import EmailMessage

    data = {
        'username': username,
    }

    message = loader.get_template('Minecraftable/User/confirmation-email.html').render({
        'data': urlsafe_base64_encode(force_bytes(data)),
        'path': base_path,
    })

    from Minecraftable.admin import EMAIL_ADMIN

    mail = EmailMessage(
        subject='Confirmation Email',
        body=message,
        from_email=EMAIL_ADMIN,
        to=[email],
        reply_to=[],
    )
    mail.content_subtype = 'html'
    mail.send()
    print_info('Confirmation Email send successfully!')