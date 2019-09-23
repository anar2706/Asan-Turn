
from django.urls import path,re_path,include

from .views import OperatorView,OperDetailView

app_name = 'oper'

urlpatterns = [

    path('',OperatorView.as_view(),name='create'),
    path('<int:pk>/',OperDetailView.as_view(),name='detail'),


]


