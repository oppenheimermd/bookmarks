from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #post views
    #path('login/', views.user_login, name='login'),
    #   Use Django authentication
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # dashboard
    path('', views.dashboard, name='dashboard'),
]