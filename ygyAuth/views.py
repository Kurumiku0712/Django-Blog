from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from .models import EmailCodeModel

import random


@require_http_methods(['GET', 'POST'])
def blog_login(request):
    """
    Login.
    """

    if request.method == 'GET':
        return render(request, 'login.html')

    form = LoginForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        remember = form.cleaned_data.get('remember')
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            login(request, user)
            if not remember:
                # If click "Remember me" the session expires after 2 weeks
                request.session.set_expiry(0)  # Session expires at browser close
            return redirect('/')  # Redirect to home on success

        # If user does not exist or invalid password
        else:
            print('Invalid email address or password.')
            messages.error(request, 'Invalid email address or password.')
            return redirect(reverse('ygyAuth:login'))
    # If invalid form
    else:
        print(form.errors)
        messages.error(request, form.errors)
        return render(request, 'login.html')


def blog_logout(request):
    """
    Logout.
    """

    logout(request)
    return redirect('/')


@require_http_methods(['GET', 'POST'])
def register(request):
    """
    Register.
    """

    if request.method == 'GET':
        return render(request, 'register.html')

    form = RegisterForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        # create_user method will encrypt the password
        User.objects.create_user(username=username, email=email, password=password)
        return redirect(reverse('ygyAuth:login'))
    else:
        print(form.errors)
        messages.error(request, form.errors)
        return render(request, 'register.html')


def send_email_code(request):
    """
    Generate and send email_code.
    """

    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400, 'message': 'Please input your email address!'})

    email_code = ''.join(random.sample('0123456789', 4))
    send_mail('Email code for blog registration',
              message=f'Your code is:{email_code}',
              recipient_list=[email],
              from_email=None)

    EmailCodeModel.objects.update_or_create(email=email, defaults={'email_code': email_code})
    return JsonResponse({'code': 200, 'message': 'Verification code sent successfully!'})
