from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from accounts import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.leaderboard, name="leaderboard"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
]