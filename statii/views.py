from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from statii.models import Statie


class StatiiView(ListView):
    template_name = "lista_statii.html"
    model = Statie
