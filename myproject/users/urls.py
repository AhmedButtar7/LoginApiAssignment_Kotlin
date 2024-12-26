# your_app/urls.py
from django.urls import path
from .views import SignUpView, LoginView, ForgotPasswordView, AllUsersView

urlpatterns = [
    path('api/users/signup/', SignUpView.as_view(), name='signup'),
    path('api/users/login/', LoginView.as_view(), name='login'),
    path('api/users/forgot/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('api/users/all/', AllUsersView.as_view(), name='all-users'),
]
