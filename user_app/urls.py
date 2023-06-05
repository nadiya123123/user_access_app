from django.urls import path
from . import views

urlpatterns=[

    path('register/', views.register, name='register'),
    path('', views.login, name='login'),
    path('newpage/', views.newpage, name='newpage'),
    path('logout/', views.logout_view, name='logout')
]