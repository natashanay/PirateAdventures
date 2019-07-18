from django.conf.urls import url
from . import views
  #login and registration routes                  
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^login$', views.login)
]
