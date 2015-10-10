from django.conf.urls import url

from . import views

urlpatterns = [
	# Person urls
    url(r'^$', views.PersonListView.as_view(), name='index'),
    url(r'^list/$', views.PersonListView.as_view(), name='person_list'),
    url(r'^create/$', views.PersonCreateView.as_view(), name='person_create'),
    url(r'^detail/(?P<pk>\d+)/$', views.PersonDetailView.as_view(), name='person_detail'),
    url(r'^update/(?P<pk>\d+)/$', views.PersonUpdateView.as_view(), name='person_update'),
    url(r'^delete/(?P<pk>\d+)/$', views.PersonDeleteView.as_view(), name='person_delete'),

    # Log urls
    url(r'^logs/$', views.LogListView.as_view(), name='log_list'),
]