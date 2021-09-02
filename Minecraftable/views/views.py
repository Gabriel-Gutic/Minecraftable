from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
import ast

from Minecraftable.forms import LoginForm, RegisterForm, ResetPasswordForm
from Minecraftable.models import Datapack, User
from Minecraftable.printer import Error, print_info


def home(request):
    template =  loader.get_template('Minecraftable/Home-Page.html')

    if request.method == 'POST':
        if 'datapack-delete' in request.POST:
            datapack_id = int(request.POST.get('datapack-id'))
            datapack = Datapack.objects.get(id=datapack_id)
            datapack_name = datapack.name
            datapack.delete()

            print_info("Datapack %s deleted", datapack_name)

            return JsonResponse({}, status=200)

    user = request.user
    datapacks = []

    if user.is_authenticated:
        datapacks = Datapack.objects.filter(user=user)

    context = {
        'datapacks': datapacks,
    }

    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('Minecraftable/User/login.html')

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username_email = form.cleaned_data['username_email']

            error_message = 'Invalid login data!'
            try:
                user = User.objects.get(username=username_email)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(email=username_email)
                except User.DoesNotExist:
                    messages.error(request, error_message)
                    return redirect('/Minecraftable/login/')
            
            password = form.cleaned_data['password']
            result = check_password(password, user.password)
            if result and user.is_active:
                auth_login(request, user)
                remember_me = request.POST.get('remember_me')
                if  not remember_me:
                    request.session.set_expiry(7200) #one hour
                    request.session.modified = True
                else:
                    request.session.set_expiry(None) #unlimited time
                    request.session.modified = True
                next = request.GET.get('next')
                if next == "/Minecraftable/logout/" or next == None or next == "/Minecraftable/login/" or next == "/Minecraftable/register/":
                    return redirect("/Minecraftable/home/")
                return HttpResponseRedirect(next)
            else:
                messages.error(request, error_message)
                return redirect('/Minecraftable/login/')



    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def register(request):
    template = loader.get_template('Minecraftable/User/register.html')

    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_again = form.cleaned_data['password_again']

            result = User.validation(username=username, email=email, password=password, password_again=password_again)
            if result is not None:
                result.print()
                messages.error(request, result)
                return redirect('/Minecraftable/register/')
            
            user = User.create_user(email=email, username=username, password=password)
            auth_login(request, user)

            #Send confirmation email
            from django.core.mail import EmailMessage

            data = {
                'username': username,
            }

            register_path = request.build_absolute_uri(request.path)
            message = loader.get_template('Minecraftable/User/confirmation-email.html').render({
                'data': urlsafe_base64_encode(force_bytes(data)),
                'path': register_path,
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
            return HttpResponseRedirect('confirmation/')

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def register_confirmation(request):
    template = loader.get_template('Minecraftable/User/register-confirmation.html')

    context = {}

    return HttpResponse(template.render(context, request))


def register_confirmed(request, data):
    template = loader.get_template('Minecraftable/User/register-confirmed.html')

    data = ast.literal_eval(urlsafe_base64_decode(data).decode("UTF-8"))

    user = User.objects.get(username=data['username'])
    user.email_confirmed = True
    user.save()

    return HttpResponse(template.render({}, request))


def not_permission(request):
    template = loader.get_template('Minecraftable/User/not-permission.html')
    return HttpResponse(template.render({}, request))


def forgot_password(request):
    template = loader.get_template('Minecraftable/User/forgot-password.html')

    if request.method == 'GET' and request.is_ajax():
        text = request.GET.get('text')

        user = User.find_user(text)
        if type(user) == Error:
            user.print()
            return JsonResponse({'error': user.get_error_message()}, status=200)
        
        from django.core.mail import EmailMessage

        data = {
            'username': user.username,
        }
        register_path = request.build_absolute_uri(request.path)
        message = loader.get_template('Minecraftable/User/password-recovery-email.html').render({
            'data': urlsafe_base64_encode(force_bytes(data)),
            'path': register_path,
        })
        from Minecraftable.admin import EMAIL_ADMIN
        mail = EmailMessage(
            subject='Password Recovery',
            body=message,
            from_email=EMAIL_ADMIN,
            to=[user.email],
            reply_to=[],
        )
        mail.content_subtype = 'html'
        mail.send()
        print_info('Password Recovery Email send successfully!')
        return JsonResponse({}, status=200)

    return HttpResponse(template.render({}, request))


def reset_password(request, data):
    template = loader.get_template('Minecraftable/User/reset-password.html')
    
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            data = ast.literal_eval(urlsafe_base64_decode(data).decode("UTF-8"))

            user = User.objects.get(username=data['username'])

            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('/Minecraftable/home/')

    form = ResetPasswordForm()

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def recovery_email_send(request):
    template = loader.get_template('Minecraftable/User/recovery-email-send.html')

    return HttpResponse(template.render({}, request))

