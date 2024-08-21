from django.shortcuts import render
from .forms import UserRegistationForm, UserLoginForm, UserProfileForm, UserSettingsForm
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView
from .models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, 'index.html')

class UserRegistationView(CreateView):
    model = User
    form_class = UserRegistationForm
    template_name = 'reg.html'
    success_url = reverse_lazy('login')

class UserLoginView(LoginView):
    template_name = 'login.html'
    form_class = UserLoginForm





class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,)) # Вызываем айдишник пользователя
    


class SettingsView(UpdateView):
    model = User
    form_class = UserSettingsForm
    template_name = 'settings.html'
    def get_success_url(self):
        return reverse_lazy('settings', args=(self.object.id,))

