from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User

class UserRegistationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя '}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя '}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))





    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control-input", 'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': "form-control-input", 'placeholder': 'Пароль пользователя'}))
    
    class Meta:
         model = User
         fields = ('username', 'password')




class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'custom-text-status1', 'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'custom-text-status2', 'placeholder': 'Фамилия'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={ 'class': 'custom-file-input'}), required=False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image')




class UserSettingsForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Сменить имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Сменить Фамилию'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Сменить почту'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Сменить пароль'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Сменить Username'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={ 'class': 'custom-file-input'}), required=False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'username', 'image')