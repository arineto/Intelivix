from math import floor, ceil

from django.utils import timezone

class TotalTimeMixin(object):

    def get_context_data(self, **kwargs):
        
        context = super(TotalTimeMixin, self).get_context_data(**kwargs)

        workload = context['object']
        actions = workload.actions.all().order_by('time')

        total_time = 0
        start_time = None
        
        for action in actions:
            if action.status == 0:
                start_time = action.time
            else:
                if start_time is not None:
                    total_time += calculate_minutes(start_time, action.time)
                    start_time = None

        if start_time is not None:
            total_time += calculate_minutes(start_time, timezone.now())

        f_hours = total_time / 60
        i_hours = floor(f_hours)
        i_minutes = ceil((f_hours - i_hours) * 60)

        context['total_worked_time'] = '%d hora(s) e %d minuto(s).' % (i_hours, i_minutes)

        return context


def calculate_minutes(start_time, end_time):
    
    diff = end_time - start_time
    minutes = float(diff.total_seconds()) / 60

    return minutes