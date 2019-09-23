
from django.urls import path,re_path,include

from .views import TurnView,TurnDetailView

app_name = 'turn'

urlpatterns = [

    path('',TurnView.as_view(),name='create'),
    path('<int:pk>/',TurnDetailView.as_view(),name='detail'),


]
