from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from django.utils.http import urlsafe_base64_decode
import json
import ast

from Minecraftable.forms import LoginForm, RegisterForm, ResetPasswordForm
from Minecraftable.models import Datapack, User, Recipe, Tag
from Minecraftable.printer import Error, print_info
from Minecraftable.decorators import login_not_required, login_required
from Minecraftable.utils import reset_password_send, reset_email_send, send_confirmation_email


def home(request):
    template =  loader.get_template('Minecraftable/Home-Page.html')

    if request.method == 'POST' and request.is_ajax():
        if 'datapack-delete' in request.POST:
            datapack_id = int(request.POST.get('datapack-id'))
            datapack = Datapack.objects.get(id=datapack_id)
            datapack_name = datapack.name
            datapack.delete()

            print_info("Datapack '" + datapack_name + "' deleted")

            return JsonResponse({"datapack_id": datapack_id}, status=200)
        elif 'tag-delete' in request.POST:
            tag_id = int(request.POST.get('tag-id'))
            tag = Tag.objects.get(id=tag_id)
            tag_name = tag.name
            tag.delete()

            print_info("Tag '" + tag_name + "' deleted")

            return JsonResponse({"tag_id": tag_id}, status=200)

    user = request.user
    datapacks = []
    tags = []
    
    if user.is_authenticated:
        datapacks = Datapack.objects.filter(user=user)
        tags = Tag.objects.filter(user=user)

    context = {
        'datapacks': datapacks,
        'tags': tags,
    }

    return HttpResponse(template.render(context, request))

@login_required()
def profile(request):

    user = request.user
    if request.method == 'GET' and request.is_ajax():
        if 'change-email' in request.GET:
            if user.email_confirmed:
                url = request.get_host() + '/reset-email/'
                reset_email_send(url, user.username, user.email)
                print_info('Reset Email send successfully!')
            else:
                return JsonResponse({'error': "Sorry, the last email associated with this account was not confirmed. So you can't reset your email until you confirm it. Please check out your email history to find your confirmation email"}, status=200)
        elif 'change-password' in request.GET:
            if user.email_confirmed:
                url = request.get_host() + '/reset-password/'
                reset_password_send(url, user.username, user.email)
                print_info('Password Reset Email send successfully!')
            else:
                return JsonResponse({'error': "Sorry, the last email associated with this account was not confirmed. So you can't reset your pasword until you confirm it. Please check out your email history to find your confirmation email"}, status=200)

    if request.method == 'POST':
        if request.is_ajax():
            image = request.FILES.get('image')
            user.image = image
            user.save()
            
            response_data = {
                'url': user.image.url,
            }
            return HttpResponse(json.dumps(response_data))

    template = loader.get_template('Minecraftable/User/profile.html')

    datapacks =  Datapack.objects.filter(user=request.user)

    count = 0
    for datapack in datapacks:
        count += Recipe.objects.filter(datapack=datapack).count()

    context = {
        'datapack_number': datapacks.count(),
        'recipe_number': count,
    }

    return HttpResponse(template.render(context, request))

@login_not_required()
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
                    return redirect('/login/')
            
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
                if next == "/logout/" or next == None or next == "/login/" or next == "/register/":
                    return redirect("/home/")
                return HttpResponseRedirect(next)
            else:
                messages.error(request, error_message)
                return redirect('/login/')



    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


@login_not_required()
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
                return redirect('/register/')
            
            user = User.create_user(email=email, username=username, password=password)
            auth_login(request, user)

            path = request.get_host() + '/email_confirmed/'
            send_confirmation_email(path, username, email)

            return HttpResponseRedirect('confirmation/')

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def register_confirmation(request):
    print_info('Merge')
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
        
        if not user.email_confirmed:
            return JsonResponse({'error': "Sorry, the email associated with this account was not confirmed. So you can't reset your password until you confirm it. Please check out your email history to find your confirmation email"}, status=200)

        url = request.get_host() + '/reset-password/'
        reset_password_send(url, user.username, user.email)
        print_info('Password Reset Email send successfully!')
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
            return redirect('/home/')

    form = ResetPasswordForm()

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def reset_email(request, data):
    template = loader.get_template('Minecraftable/User/reset-email.html')
    
    from Minecraftable.forms import ResetEmailForm

    if request.method == 'POST':
        form = ResetEmailForm(request.POST)
        if form.is_valid():
            data = ast.literal_eval(urlsafe_base64_decode(data).decode("UTF-8"))

            user = User.objects.get(username=data['username'])

            email = form.cleaned_data['email']

            taken = len(User.objects.filter(email=email)) > 0
            if taken:
                messages.error(request, "This email address is already taken!")
                return HttpResponseRedirect(request.path_info)

            user.email = email
            user.email_confirmed = False
            user.save()

            path = request.get_host() + '/email_confirmed/'
            send_confirmation_email(path, user.username, email)

            return redirect('/email-reset-confirmation/')

    form = ResetEmailForm()

    context = {
        'form': form,
    }

    return HttpResponse(template.render(context, request))


def recovery_email_send(request):
    template = loader.get_template('Minecraftable/User/recovery-email-send.html')

    return HttpResponse(template.render({}, request))


def email_reset_confirmation(request):
    template = loader.get_template('Minecraftable/User/email-reset-confirmation.html')

    return HttpResponse(template.render({}, request))

