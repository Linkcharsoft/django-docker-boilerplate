from django.urls import path

from users.register_views import Password_recovery_email_send, Check_token, Password_recovery_confirm,PasswordChangeViewModify, \
    FacebookLogin, GoogleLogin

from users.views import User_profile_me


urlpatterns = [
    # Account management
    path('password-change/', PasswordChangeViewModify.as_view(), name='rest_password_change'),
    path('password-recovery/', Password_recovery_email_send.as_view(), name='password_recovery_email_send'),
    path('password-recovery/check-token/', Check_token.as_view(), name='check_token'),
    path('password-recovery/confirm/', Password_recovery_confirm.as_view(), name='password_recovery_confirm'),

    path('dj-rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login'),

    # User management
    path('me/', User_profile_me.as_view(), name='user_profile_me'),

]