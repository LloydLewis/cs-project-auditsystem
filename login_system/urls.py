from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login_user, name = "login"),
    path('logout_user', views.logout_user, name = 'logout'),
]