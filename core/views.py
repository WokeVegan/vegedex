import os
from django.contrib.auth import login
from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


# Create your views here.
def about(request):
    return render(request, 'core/about.html')


# Create your views here.
def request_login(request):
    return render(request, 'core/login.html')


def activate(request, uidb64, token):
    return redirect('home')


# Create your views here.
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'core/register.html', {'form': form})

    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            user.is_active = False
            user.save()

            mail_subject = 'Activate your account.'
            message = render_to_string('core/activate_account.html', {
                'user': user.username,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'protocol': 'https' if request.is_secure() else 'http'
            })

            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            if email.send():
                messages.success(request, f"Hey there, {user}! Thanks for singing up! Please go to your email {to_email} and click on the activation link to complete the registration process.")
            else:
                messages.error(request, f"There was an error sending the verification email to {to_email}.")
            return redirect('home')
        else:
            return render(request, 'core/register.html', {'form': form})


def home(request):
    return render(request, 'core/home.html')


def handler404(request, exception):
    return render(request, 'core/404.html')
