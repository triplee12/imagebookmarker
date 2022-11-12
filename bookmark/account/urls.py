from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView,
    PasswordChangeDoneView,PasswordResetView, PasswordResetCompleteView,
    PasswordResetDoneView, PasswordResetConfirmView
)
from .views import (
    dashboard, user_login,
    register, edit, user_list, user_detail,
    user_follow
)

urlpatterns = [
    path('register/', register, name='register'),
    # path('login/', user_login, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('dashboard/', dashboard, name='dashboard'),
    path('edit/', edit, name='edit'),
    path('users/', user_list, name='user_list'),
    path('users/follow/', user_follow, name='user_follow'),
    path('users/<username>/', user_detail, name='user_detail'),
]
