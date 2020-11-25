from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from . import forms

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = 'acounts/login.html'

class MyLogoutView(LoginRequiredMixin, LoginView):
    template_name = 'acounts/logout.html'

class UserCreateView(CreateView):
    form_class = forms.UserCreate
    template_name = 'acounts/signin.html'
    success_url = reverse_lazy('login')
