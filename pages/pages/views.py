from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
class HomepageView(TemplateView):
    template_name = 'home.html'
class AboutPageView(TemplateView):
    template_name = 'about.html'