from django.urls import path
from users.apps import UsersConfig
from users.views import UserRegisterView, UserLoginView, UserLogoutView, email_verification, UserPasswordResetView, \
    UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('confirm-email/<str:token>/', email_verification, name='confirm-email'),
    path('recovery/', UserPasswordResetView.as_view(), name='recovery'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
]
