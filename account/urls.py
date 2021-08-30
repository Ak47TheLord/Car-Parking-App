from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', parkView, name='parkView'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='account/include/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/include/logout.html'), name='logout'),
    # path('park/', park, name='parkin')
    path('home', homeView, name='homeView'),
    path('slots/', slots, name='slots'),
    path('slots/<int:slot_id>/unpark', unpark_slot, name='un-park-slot'),
    # path('<slug:meetup_slug>', information, name='information-detail'),

]

