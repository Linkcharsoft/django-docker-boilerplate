from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.account.views import ConfirmEmailView
from rest_auth.registration.views import SocialLoginView, RegisterView
from dj_rest_auth.registration.serializers import VerifyEmailSerializer

from django_base.settings import BASE_URL, EMAIL_HOST_USER, YOUR_APP_NAME
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail 
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from datetime import timedelta
from django.utils import timezone


from users.models import User_profile,User, TokenRecovery
from users.utils import get_random_string
from users.serializers import User_profile_serializer, User_serializer


# Create your views here.



class User_profile_me(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            profile_serializer = User_profile_serializer(request.user.user_profile)
            user_serializer = User_serializer(request.user) 
            return Response({'user':user_serializer.data, 'user_profile':profile_serializer.data})
        else:
            return Response({'data': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def patch(self, request):
        if request.user.is_authenticated:
            user_serializer = User_serializer(data=request.data, instance=request.user, partial=True)
            if user_serializer.is_valid():
                profile_serializer = User_profile_serializer(data=request.data, instance=request.user.user_profile, partial=True)
                if profile_serializer.is_valid():
                    user_serializer.save()
                    profile_serializer.save()

                    return Response({'user':user_serializer.data, 'user_profile':profile_serializer.data})
        
                else:
                    return Response(profile_serializer.errors)
            else:
                return Response(user_serializer.errors)
        else:
            return Response({'data': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)

