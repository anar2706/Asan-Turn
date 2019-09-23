from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse

from django.views.generic import CreateView,DetailView,TemplateView
from .models import Operator

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'



class OperatorView(CreateView):
    template_name = 'operator_create.html'
    model = Operator
    fields = ['name','surname','service','image']




class OperDetailView(DetailView):
    model = Operator
    template_name = 'oper_detail.html'
    context_object_name = 'operator'
    


