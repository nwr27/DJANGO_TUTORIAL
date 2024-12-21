from django.conf.urls import url, include
from django.contrib import admin
from . import views
from contact import views as contactViews 
from prime import views as primeViews 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^about/$', views.about),
    url(r'^blog/', include('blog.urls')),
    url(r'^contact/$', contactViews.index),
    url(r'^prime/$', include('prime.urls')),

]
