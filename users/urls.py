from django.urls import path
from . import views

urlpatterns = [
    path('email', views.login_email, name='login-email'),
    path('password', views.login_password, name='login-password'),
    path('logout', views.logout_view, name='logout'),
    path('signup', views.signup, name='signup'),
    path('password-reset', views.password_reset, name='password-reset'),
    path('activate/<uidb64>/<token>', views.activate, name='activate')
]
