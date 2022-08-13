from django.conf.urls import url
from django.urls import path
from .views import login_view, register_as_problem_statement_creator, logout_view, otp_validity, change_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/ps_creator', register_as_problem_statement_creator, name="register-psc"),
    path('logout/', logout_view, name="logout"),
    path('email_verification/', otp_validity, name="email_verification"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='reset_password.html',
             subject_template_name='password_reset_subject.txt',
             email_template_name='password_reset_email_content.txt',
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='reset_password_email_sent.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='reset_new_password.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='reset_password_success.html'
         ),
         name='password_reset_complete'),
    path('change_password/', change_password, name="change-password")
]
