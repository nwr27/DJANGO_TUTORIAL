from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hallo Dunia")

def about(request):
  return HttpResponse("Ini About")

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^about/$', about),

]
