from  django.urls import re_path, include

from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    re_path('signup/', views.SignUp.as_view(), name='signup'),
    re_path(r'^password_change/$',
        PasswordChangeView.as_view(template_name='registration/password_change.html'),
        name='password_change'),
    re_path(r'^password_reset/$',
        PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
        name='password_reset'),
    re_path(r'^password_reset_done/$',
        PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),
    re_path(r'reset/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
        name='password_reset_confirm'),
    re_path(r'^reset/done/$',
        PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
]