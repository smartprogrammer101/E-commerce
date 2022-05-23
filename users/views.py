from smtplib import SMTPConnectError
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignInEmailForm, SignInPasswordForm, RegistrationForm
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            # form.check_password_match()
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            if password and password2 and password != password2:
                messages.error(request, 'Passwords did not match!')
                return render(request, 'users/signup.html', {'form': form})
            user.set_password(password)
            user.is_active = False
            user.save()

            #Sending email confirmation message
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={
                'uidb64':uidb64, 'token': token_generator.make_token(user)})
            activate_url = 'http://'+domain+link
            email_body = 'Hi! you can use this link to activate your ezone account'
            email_subject = 'Activate your Ezone account\n' + activate_url

            message = EmailMessage(
                email_subject,
                email_body,
                'user@email.com',
                [user.email]
            )
            try:
                message.send(fail_silently=False)
            except SMTPConnectError:
                messages.error(request, 'something went wrong!')
                return render(request, 'users/signup.html', {'form': form})

            return redirect('login-email')
        else:
            return render(request, 'users/signup.html', {'form': form})


    form = RegistrationForm()
    return render(request, 'users/signup.html', {'form': form})


def activate(request, uidb64, token):
    return redirect('login')




















def login_email(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignInEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            User = get_user_model()
            user = User.objects.filter(email=email).exists()

            if user:
                request.session['email'] = email
                return redirect('login-password')
                
            messages.error(request, 'This email is not associated with any Ezone account.\n Are you trying to <a href="#" class="inline">sign up?</a>')


    form = SignInEmailForm()
    return render(request, 'users/login-email.html', {'form': form})

def login_password(request):
    email = request.session.get("email")
    if request.method == 'POST':
        form = SignInPasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
        User = get_user_model()
        user = User.objects.get(email=email)
        if not user.is_active:
            return render(request, 'users/inactive-user.html')
        user = authenticate(request, email=email, password=password)
        if user:
            print(user.username)
            login(request, user)
            return redirect('home')
        
        messages.error(request, 'Password is incorrect!')
        return render(request, 'users/login-password.html', {'form': form, 'email': email})
        
    form = SignInPasswordForm()
    return render(request, 'users/login-password.html', {'form': form, 'email': email})


def password_reset(request):
    return render(request, 'users/password-reset.html')

def logout_view(request):
    logout(request)
    return redirect('login-email')