from django.conf.urls import url

from . import views

urlpatterns = [
	# Person urls
    url(r'^$', views.PersonListView.as_view(), name='index'),
    url(r'^list/$', views.PersonListView.as_view(), name='person_list'),
    # url(r'^create/$', views.PersonCreateView.as_view(), name='person_create'),
    # url(r'^detail/(?P<person_id>\d+)/$', views.PersonDetailView, name='person_detail'),
    # url(r'^update/(?P<person_id>\d+)/$', views.PersonUpdateView, name='person_update'),
    # url(r'^delete/(?P<person_id>\d+)/$', views.PersonDeleteView, name='person_delete'),

    # # Log urls
    url(r'^logs/$', views.LogListView.as_view(), name='log_list'),
]