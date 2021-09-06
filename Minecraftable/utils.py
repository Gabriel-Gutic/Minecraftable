from posixpath import dirname
from django.template import loader

from Minecraftable.printer import print_info


def zip_from_directory(dir_path):
    from zipfile import ZipFile
    import zipfile
    import os
    from os.path import basename

    zip_path = dir_path + ".zip"
    location = dir_path[:len(dir_path) - len(basename(dir_path))]
    with ZipFile(zip_path, 'w') as zip_file:
        for folderName, subFolders, fileNames in os.walk(dir_path):
            zfi = zipfile.ZipInfo(folderName.replace(location, '', 1))
            zfi.external_attr = 16
            zip_file.writestr(zfi, '')
            for fileName in fileNames:
                filePath = os.path.join(folderName, fileName)
                zip_file.write(filePath, filePath.replace(location, "", 1))
        zip_file.close()
        return zip_file.filename


def remove_files_that_contain(text):
    from django.core.files.storage import FileSystemStorage
    from django.conf import settings as django_settings

    fs = FileSystemStorage()
    dirs, files = fs.listdir(django_settings.MEDIA_ROOT)
    for file in files:
        if text in str(file):
            fs.delete(file)


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