from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import TemplateView


class ViewTemplate(TemplateView):
    template_name = 'shop/register.html'


class UserRegisterView(CreateView):
    template_name = 'shop/register.html'

