from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class Workload(models.Model):

    user = models.ForeignKey(User)
    day = models.DateField()
    actions = models.ManyToManyField('Action')

    def __str__(self):
        return "%s (%s)" % (self.user, self.day)

    def get_absolute_url(self):
        return reverse(
            'workload:workload_detail', args=[self.pk]
        )

    class Meta:
        verbose_name = 'Carga Horária'
        verbose_name_plural = 'Cargas Horária'
        ordering = ['day', 'user']


class Action(models.Model):

    ACTION_STATUS = (
        (0, 'Start'),
        (1, 'Stop'),
    )

    time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=ACTION_STATUS)

    def __str__(self):
        return "%s (%s)" % (self.time, self.status)

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'
        ordering = ['time', 'status']