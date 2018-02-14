from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.party_list, name='party_list'),
    url(r'(?P<pk>\d+)/$', views.party_detail),
    url(r'^post_party/$', views.post_party, name="post_party"),
]
