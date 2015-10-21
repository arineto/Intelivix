from django.conf.urls import url

from . import views

urlpatterns = [
    # Person urls
    url(r'^$', views.WorkloadListView.as_view(), name='index'),
    url(r'^list/$', views.WorkloadListView.as_view(), name='workload_list'),
    url(r'^detail/(?P<pk>\d+)/$', views.WorkloadDetailView.as_view(), name='workload_detail'),

    url(r'^create_action/$', views.ActionCreateView.as_view(), name='action_create'),
]