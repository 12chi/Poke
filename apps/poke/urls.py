from django.conf.urls import url
import views

urlpatterns = [
    url(r'^main$', views.index),
    url(r'^pokes$', views.pokes),
    url(r'^add_poke/(?P<uid>\d+)$', views.add_poke),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^reset$', views.reset),  
    url(r'^success$', views.success),
]