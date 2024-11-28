import random
import string
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from api import serializer as api_serializer
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from userauths.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from lms_backend import settings    

def generate_otp():
    otp = ''.join(random.choices(string.digits, k=6))
    return otp


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = api_serializer.RegisterSerializer

class PasswordResetEmailVerifyAPIView(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = api_serializer.UserSerializer
    def get_object(self):
        email = self.kwargs['email']
        user = User.objects.filter(email=email).first()
        if user:
            uuidb64 = user.pk
            token = RefreshToken.for_user(user)
            refresh_token = str(token.access_token)

            user.otp = generate_otp()
            user.refresh_token = refresh_token
            user.save()
            
            link = f"http://localhost:5173/create-new-password/?otp={user.otp}&uuidb64={uuidb64}&token={refresh_token}"
            
            context = {
                "link": link,
                "username": user.username
            }
            subject = "Password Reset"
            html_content = render_to_string("email/password_reset_email.html", context)
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                subject, text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            email.attach_alternative(html_content, "text/html")
            email.send()

        return user
    
class PasswordChangeAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = api_serializer.UserSerializer

    def create(self, request, *args, **kwargs): 
        otp = request.data['otp']
        uuidb64 = request.data['uuidb64']
        password = request.data['password']
        user = User.objects.filter(id=uuidb64).first()
        if user.otp == otp:
            user.set_password(password)
            user.otp = None
            user.save()
            return Response({'message': 'Password changed successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        