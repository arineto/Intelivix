from datetime import datetime

from django.shortcuts import render_to_response, redirect
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import View

from .models import *
from .mixins import *


class WorkloadListView(ListView):

    model = Workload

    def get_queryset(self):
        user = self.request.user
        today = datetime.today()
        
        try:
            Workload.objects.get(user=user, day=today)
        except Workload.DoesNotExist:
            Workload.objects.create(user=user, day=today)

        return Workload.objects.all()


class WorkloadDetailView(TotalTimeMixin, DetailView):

    model = Workload


class ActionCreateView(View):

    def post(self, request, *args, **kwargs):

        status = request.POST.get('status')
        workload_id = request.POST.get('workload_id')
        workload = Workload.objects.get(id=workload_id)

        action = Action.objects.create(status=status)
        workload.actions.add(action)
        workload.save()

        return redirect(workload.get_absolute_url())
