from django.shortcuts import render
from lab import models
from django.views.generic import ListView

# Create your views here.

class Index(ListView):
    model=models.People
    queryset = model.objects.all()
    template_name = 'index.html'
    context_object_name = 'data'
