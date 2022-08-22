from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('engine.urls')),
]

from django.urls import path
from . import views 


urlpatterns = [
    path('',views.query, name="query"),
    path('results', views.results, name="results"),
    path('about', views.about, name="about"),
]