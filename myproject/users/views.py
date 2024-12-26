from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from .serializers import UserSerializer
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
import json
from django.core.mail import send_mail


 # Make sure this is your custom user model
from django.conf import settings
# SignUp View to handle user registration
class SignUpView(APIView):  # Inheriting from APIView to make it easier to handle requests
    def post(self, request):
        try:
            data = request.data
            email = data.get('email')
            password = data.get('password')
            username = data.get('username')
            
            # Validate that required fields are provided
            if not email or not password or not username:
                return Response({'error': 'Please provide all required fields: email, password, and username'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the user already exists
            if CustomUser.objects.filter(email=email).exists():
                return Response({'error': 'Email already in use'}, status=status.HTTP_400_BAD_REQUEST)

            # Hash the password before saving it to the database
            hashed_password = make_password(password)

            # Create the user
            user = CustomUser.objects.create(
                email=email,
                password=hashed_password,
                username=username
            )

            # Optional: Send a welcome email (you can customize the email content)
            send_mail(
                'Welcome to Our App!',
                'Thank you for signing up!',
                'admin@example.com',
                [email],
            )

            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Login View to handle user authentication
class LoginView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')

            # Authenticate the user using username and password
            user = authenticate(username=username, password=password)

            if user is not None:
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Forgot Password View to handle password reset email


class ForgotPasswordView(APIView):
    def post(self, request):
        try:
            # Extract email from request
            email = request.data.get('email')
            
            # Validate the email
            if not email:
                return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the user exists in the database
            user = CustomUser.objects.filter(email=email).first()

            if user:
                # Simulate sending a reset link (Implement a real link if necessary)
                reset_link = "http://example.com/reset-password"  # Generate real reset link here
                send_mail(
                    'Password Reset Request',
                    f'Click the link to reset your password: {reset_link}',
                    settings.DEFAULT_FROM_EMAIL,  # Make sure you have DEFAULT_FROM_EMAIL in your settings.py
                    [email],
                )
                return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
            else:
                # If the email does not exist in the database
                return Response({'error': 'Email not registered'}, status=status.HTTP_404_NOT_FOUND)
        
        except Exception as e:
            # Handle unexpected errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# AllUsers View to fetch all registered users
class AllUsersView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
