import email
from django.shortcuts import render, redirect
from .forms import SignInEmailForm, SignInPasswordForm, RegistrationForm
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib import messages

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
            return redirect('login-email')
        else:
            return render(request, 'users/signup.html', {'form': form})


    form = RegistrationForm()
    return render(request, 'users/signup.html', {'form': form})























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