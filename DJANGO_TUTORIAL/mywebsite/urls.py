from django.conf.urls import url
from django.contrib import admin
from . import views
from blog import views as blogViews 
from contact import views as contactViews 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^about/$', views.about),
    url(r'^blog/$', blogViews.index),
    url(r'^contact/$', contactViews.index),

]
