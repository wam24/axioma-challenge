from django.contrib.auth.decorators import login_required
from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home', login_required(views.Home.as_view(), login_url=''), name='home'),
    path('logout', login_required(views.logout_view), name='logout')
    ]
