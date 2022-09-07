from django.db.models import fields
from django.views.generic import ListView, DetailView, CreateView
from .models import Menu
from django.contrib.auth.mixins import LoginRequiredMixin

class MenuListView(ListView):
    model = Menu

class MenuDetailView(DetailView):
    model = Menu

