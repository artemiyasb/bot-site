from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('reg', views.UserRegistationView.as_view(), name='reg'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('profile/<int:pk>/', login_required(views.ProfileView.as_view()), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/', include('allauth.urls')),
    path('settings/<int:pk>/', views.SettingsView.as_view(), name='settings'),

]