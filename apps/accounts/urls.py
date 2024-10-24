from django.urls import path
from .views import UserRegistrationView, UserLoginView, ProfileView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    # profile
    path('profile/', ProfileView.as_view(), name='profile'),
]
