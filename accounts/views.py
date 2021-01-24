from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy
from . import forms




class SignCreateView(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/signup.html"

