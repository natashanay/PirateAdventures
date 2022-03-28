from django.conf.urls import url
from . import views
  #login and registration routes                  
urlpatterns = [  

  #render routes- these routes display template pages
      url(r'^edit/(?P<adventure_id>\d+)$', views.Update),
      url(r'^adventures/(?P<adventure_id>\d+)$', views.Read),
      url(r'^adventures/new$', views.Create),
      url(r'^dashboard$', views.Dashboard),

#redirect or hidden or process routes
    url(r'^cancelAdventure/(?P<adventure_id>\d+)$', views.CancelAdventure),
    url(r'^adventures/process_create$', views.ProcessCreate),

    url(r'^adventures$', views.ProcessDashboard),
    # url(r'^processUpdate$', views.ProcessUpdate),
    url(r'^processUpdate/(?P<adventure_id>\d+)$', views.ProcessUpdate),

    # url(r'^joinAdventure$', views.ProcessJoin),
    url(r'^removeAdventure/(?P<adventure_id>\d+)$', views.RemoveAdventure),
    url(r'^joinAdventure/(?P<adventure_id>\d+)$', views.ProcessJoin),

  #this is most basic route...least specific about url so it goes at the bottom
    url(r'^$', views.PirateAdventure),

]

