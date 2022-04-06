from . import views
from django.urls import path

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('Myadmin/', views.AdminView.as_view(),name='Myadmin'),
    path('register/', views.registerPage,name='register'),
    path('login/' , views.loginPage , name='login' ),
    path('logout/', views.logoutUser , name='logout' )
]