from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # account
    path('accounts/', include('django.contrib.auth.urls')),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='account/password.html'), name='password_account'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_done.html'), name='password_change_done'),
    # login
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    # path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    # password change
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_reset_form.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_change_form.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    # register new user
    path('register/', views.register, name='register'),
    # edit user profile
    path('edit/', views.edit, name='edit'),
    # dashboard
    path('', views.dashboard, name='dashboard'),

]
