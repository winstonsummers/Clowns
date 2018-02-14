from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.party_list, name='party_list'),
]
