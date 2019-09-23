
from django.contrib import admin
from django.urls import path,re_path,include
from turn.views import home_view,TurnApiList
from django.conf import settings
from operators.views import HomeView
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('operator/',include('operators.urls',namespace='oper')),
    path('turn/',include('turn.urls',namespace='turn')),
    path('json/',home_view,name='home'),
    path('api/',TurnApiList.as_view(),name='api'),
    path('',HomeView.as_view(),name='home')

]

if settings.DEBUG :
    urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

