from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
import ast

from Minecraftable.forms import NewDatapackForm, LoginForm, RegisterForm
from Minecraftable.models import Datapack, User, Client
from Minecraftable.printer.error import Error


def home(request):
    
    template =  loader.get_template('Minecraftable/Home-Page.html')

    user = request.user
    datapacks = []

    if user.is_authenticated:
        datapacks = Datapack.objects.filter(client=Client.objects.get(user=user))

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
                    request.session.set_expiry(None)
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

            result = Client.validation(username=username, email=email, password=password, password_again=password_again)
            if result is not None:
                result.print()
                messages.error(request, result)
                return redirect('/Minecraftable/register/')
            
            #Send confirmation email
            from django.core.mail import EmailMessage

            data = {
                'username': username,
                'email': email,
                'password': password,
            }

            register_path = request.build_absolute_uri(request.path)
            message = loader.get_template('Minecraftable/User/confirmation-email.html').render({
                'data': urlsafe_base64_encode(force_bytes(data)),
                'path': register_path,
            })

            from .admin import EMAIL_ADMIN
            mail = EmailMessage(
                subject='Confirmation Email',
                body=message,
                from_email=EMAIL_ADMIN,
                to=[email],
                reply_to=[],
            )

            mail.content_subtype = 'html'
            mail.send()
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

    Client.create_client(data['email'], data['username'], data['password'])

    return HttpResponse(template.render({}, request))

