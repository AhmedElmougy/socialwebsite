from django.shortcuts import render
from django.views.generic import CreateView,TemplateView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"

