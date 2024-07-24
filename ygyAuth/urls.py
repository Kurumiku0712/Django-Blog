from django.urls import path
from ygyAuth import views

app_name = 'ygyAuth'

urlpatterns = [

    path('login/', views.blog_login, name='login'),
    path('logout/', views.blog_logout, name='logout'),

    path('register/', views.register, name='register'),

    path('verification/', views.send_email_code, name='send_email_code'),


]
