
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/<str:username>",views.profile,name="profile"),
    path("following",views.following,name="following"),
    path("user_request",views.user_request,name="user_request"),
    path("edit",views.edit,name="edit"),
    path("likes/<str:post>",views.likes,name="likes")
]
