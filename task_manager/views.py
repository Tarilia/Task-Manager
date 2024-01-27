from django import forms
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "index.html"


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    next_page = reverse_lazy("index")
