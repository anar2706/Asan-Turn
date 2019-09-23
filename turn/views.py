from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,DetailView
from django.http import JsonResponse
from operators.models import Operator
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import TurnSerializer
from rest_framework import generics


from .models import Order
# Create your views here.

class TurnView(CreateView):
    model = Order
    template_name = 'turn_create.html'
    fields = ['name','surname','service']
    def form_valid(self,form):
        resp = super().form_valid(form)
        form.save()
        return resp




class TurnDetailView(DetailView):
    model = Order
    template_name = 'turn_detail.html'
    context_object_name = 'turn'



def home_view(request):
    person =Order.objects.filter(state=1).first()

    context = {

        'turn':person
    }

    return render(request,'test.html',context)


class TurnApiList(APIView):
        
    def post(self,request):
        person =Order.objects.filter(state=1).first()
        next_person = Order.objects.filter(state=1,id__gt=person.id).order_by('created').first()
        if  next_person:
            arr = [person,next_person]
            serializer = TurnSerializer(arr,many=True)
        else:
            serializer = TurnSerializer(person)
        permission_classes = [AllowAny,]
        oper = request.POST.get('op_id')
        oper_obj = Operator.objects.get(id=oper)
        person.operator = oper_obj
        person.state = 2
        person.save()
        return Response(serializer.data)

    def get(self,request):
        person  =Order.objects.filter(state=1).first()
        next_person = Order.objects.filter(state=1,id__gt=person.id).order_by('created').first()
        if  next_person:
            arr      = [person,next_person]
            serializer  = TurnSerializer(arr,many=True)
        else:
            serializer = TurnSerializer(person)
        permission_classes = [AllowAny,]
        return Response(serializer.data)


